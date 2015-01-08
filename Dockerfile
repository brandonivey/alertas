FROM ubuntu:14.10

# Install Python Setuptools
RUN apt-get update
RUN apt-get install -y python-setuptools
RUN apt-get install -y docker.io

# Install pip
RUN easy_install pip

# Add and install Python modules
ADD requirements.txt /src/requirements.txt
RUN cd /src; pip install -r requirements.txt

# Bundle app source
ADD . /src

# Expose
EXPOSE  5000

WORKDIR /src

# Run
CMD ["python", "run.py"]
