# -*- coding: utf-8 -*-

"""
    eve-demo settings
    ~~~~~~~~~~~~~~~~~

    Settings file for our little demo.

    PLEASE NOTE: We don't need to create the two collections in MongoDB.
    Actually, we don't even need to create the database: GET requests on an
    empty/non-existant DB will be served correctly ('200' OK with an empty
    collection); DELETE/PATCH will receive appropriate responses ('404' Not
    Found), and POST requests will create database and collections when needed.
    Keep in mind however that such an auto-managed database will most likely
    perform poorly since it lacks any sort of optimized index.

    :copyright: (c) 2014 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""

import os

# Use the MongoHQ sandbox as our backend.
MONGO_HOST = 'ds031721.mongolab.com'
MONGO_PORT = 31721
MONGO_USERNAME = 'score_dbuser'
MONGO_PASSWORD = '3003SummitBlvd'
MONGO_DBNAME = 'scorecard'

# also, correctly set the API entry point
# SERVER_NAME = 'localhost'


# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20

daily = {
    # if 'item_title' is not provided Eve will just strip the final
    # 's' from resource name, and use it as the item_title.
    # 'item_title': 'daily_score',

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'unit'
    },

    'schema': {
        'page': {
            'type': 'string',
            'required': True,
        },
        'unit': {
            'type': 'string',
        },
        'count': {
            'type': 'integer',
        },
        'availability': {
            'type': 'integer',
        },
        'unit': {
            'type': 'string',
            'required': True,
        },
        'page_id': {
            'type': 'integer',
        },
        'date': {
            'type': 'datetime',
        },
        'performance': {
            'type': 'float',
        },
    }
}

# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    'daily': daily,
}
