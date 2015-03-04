import os
from contextlib import contextmanager
import time

from fabric.api import env, cd, prefix, sudo, run, task, local
from fabric.contrib.files import exists
from fabric.contrib.project import rsync_project


env.hosts = ['slab9901', 'plab2901']
env.app_name = 'alertas'
env.git_repo = "https://github.com/brandonivey/alertas.git"
env.base_path = "/data/notifications"
env.venv_path = env.base_path
env.proj_path = os.path.join(env.base_path, env.app_name)
env.archive_path = os.path.join(env.base_path, "archive")
env.user = "bivey"
env.password = ""
env.key_filename = "/Users/bcivey/.ssh/id_rsa"
env.sudo_user = "www"
env.local_path = os.path.abspath(os.path.dirname(__file__))
env.temp_path = "/tmp/%s/" % env.app_name


@contextmanager
def virtualenv():
    """
    Runs commands within the project's virtualenv.
    """
    with cd(env.venv_path):
        with prefix("source %s/bin/activate" % env.venv_path):
            yield


@contextmanager
def project():
    """
    Runs commands within the project's directory.
    """
    with virtualenv():
        with cd(env.proj_path):
            yield


@task
def pack():
    """
    create a new source distribution as tarball
    """
    with project():
        local('python setup.py sdist --formats=gztar', capture=False)


@task
def pip(reqs_path):
    """
    Installs one or more Python packages within the virtual environment.
    """
    with virtualenv():
        return sudo("pip install -r %s" % reqs_path)


@task
def deploy(**kwargs):
    if 'm' in kwargs:
        message = kwargs['m']
        local("svn ci -m '%s'" % message)
    else:
        local("echo 'WARNING: running deploy without SVN commit.\n##########'")


    # make sure the directory is there!
    if not exists(env.temp_path):
        run("mkdir -p %s" % env.temp_path)

    if not exists(env.proj_path):
        sudo("mkdir -p %s" % env.proj_path)
    else:
        archive_file = "%s-%s.tar.gz" % (env.app_name, time.time())
        if not exists(env.archive_path):
            sudo("mkdir -p %s" % env.archive_path)
        sudo("tar czvf %s/%s %s" % (env.archive_path, archive_file, env.proj_path))

    # rsync changed files to temp dir on server
    rsync_project(local_dir="%s/" % env.local_path, remote_dir=env.temp_path, exclude='*.pyc')
    # sudo as www and copy application files to live directory
    sudo("cp -r %s/* %s" % (env.temp_path, env.proj_path))
    # install python requirements
    pip("%s/requirements.txt" % env.proj_path)


@task
def run_script(script):
    with project():
        output = sudo("python %s" % script)
        print output
