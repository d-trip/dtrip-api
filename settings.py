import os

X_DOMAINS = '*'

DOMAIN = {
    'accounts': {
        'schema': {
            'name': {'type': 'string'},
            'profile': {'type': 'dict'},
            'post_count': {'type': 'integer'},
            'last_post': {'type': 'datetime'},
            'reputation': {'type': 'integer'},
        },

        'datasource': {'source': 'account_object'},
        'resource_methods': ['GET']
    },

    'posts': {
        'schema': {
            'title': {'type': 'string'},
            'author': {'type': 'string'},
            'permlink': {'type': 'string'},
            'created': {'type': 'datetime'},
            'geo': {'type': 'dict'},
        },

        'datasource': {'source': 'post_object'},
        'resource_methods': ['GET']
    }
}


PAGINATION_LIMIT = 10000


MONGO_QUERY_BLACKLIST = ['$where', '$regex']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET']

DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'


MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')
MONGO_PORT = os.getenv('MONGO_PORT', 27017)
MONGO_USERNAME = os.getenv('MONGO_USERNAME')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
MONGO_DBNAME = os.getenv('MONGO_DBNAME', 'DTripData')
MONGO_AUTH_SOURCE = os.getenv('MONGO_AUTH_SOURCE', 'admin')
