# -*- coding: utf-8 -*-

"""
    Eve Demo
    ~~~~~~~~

    A demostration of a simple API powered by Eve REST API.

    :copyright: (c) 2014 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""

import os
from eve import Eve

if __name__ == '__main__':
    port = 5000
    host = '0.0.0.0'

    app = Eve()
    app.run(host=host, port=port)
