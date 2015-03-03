# -*- coding: utf-8 -*-

"""
    eve-app
"""

import os
from eve import Eve


SETTINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.py')
port = 5000
host = '0.0.0.0'

app = Eve(settings=SETTINGS_PATH)

if __name__ == '__main__':
    app.run(host=host, port=port)
