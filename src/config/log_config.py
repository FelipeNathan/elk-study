import logging
from logging.config import dictConfig


def load_dict_config():
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] [%(levelname)s] : %(message)s'
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })

    logging.getLogger('werkzeug').setLevel(logging.ERROR)
