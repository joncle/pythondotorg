from .base import *

DEBUG = True
TEMPLATE_DEBUG = True
PYTHON_ORG_CONTENT_SVN_PATH='/Users/flavio/working_copies/beta.python.org/build/data'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}

#STATIC_ROOT = '/home/jobs/pythondotorg/static'
#STATIC_DIRFILES = '/home/jobs/pythondotorg/static'
