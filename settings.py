# -*- coding: utf-8 -*-

"""
    eve-app settings
"""


# Use the MongoHQ sandbox as our backend.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = ''
MONGO_PASSWORD = ''
MONGO_DBNAME = 'notifications'

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

# QUERY_WHERE = 'query'

units = ['ATG', 'ATC Mobile', 'Dealer Site', 'ATC', 'RealDeal', 'KBB', 'Tradein', 'vAuto', 'Fastlane', 'ATC SYC', 'VinSolution', 'HomeNet', 'ATX', 'CRM']

incident = {
    # if 'item_title' is not provided Eve will just strip the final
    # 's' from resource name, and use it as the item_title.
    # 'item_title': 'incident',

    'schema': {
        'title': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 128,
            'required': True,
        },
        'status': {
            'type': 'string',
            'allowed': ['red', 'yellow', 'green'],
            'required': True,
        },
        'unit': {
            'type': 'string',
            'allowed': units,
            'required': True,
        },
        'description': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 512,
            'required': True,
        },
        'created_by': {
            'type': 'string',
            'maxlength': 32,
        },
    }
}

update = {
    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'schema': {
        'created_by': {
            'type': 'string',
            'maxlength': 32,
        },
        'description': {
            'type': 'string',
        },
        'incident': {
            'type': 'objectid',
            'required': True,
            # referential integrity constraint: value must exist in the
            # 'incidents' collection. Since we aren't declaring a 'field' key,
            # will default to `incidents._id` (or, more precisely, to whatever
            # ID_FIELD value is).
            'data_relation': {
                'resource': 'incidents',
                # make the owner embeddable with ?embedded={"incident":1}
                'embeddable': True
            },
        },
    }
}

# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    'incidents': incident,
    'updates': update,
}
