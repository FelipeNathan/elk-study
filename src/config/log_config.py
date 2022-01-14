import logging
import sys


def load_dict_config():
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(extra)s]: %(message)s')

    stream = logging.StreamHandler(stream=sys.stdout)
    stream.setLevel(logging.INFO)
    stream.setFormatter(formatter)
    stream.addFilter(ExtraLogFilter())

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(stream)
    logger.addFilter(ExtraLogFilter())

    logging.getLogger('werkzeug').setLevel(logging.ERROR)


class ExtraLogFilter(logging.Filter):
    def filter(self, record):
        if not hasattr(record, 'extra'):
            record.extra = {}
        return True
