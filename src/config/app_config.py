import os
from elasticapm.contrib.flask import ElasticAPM
from flask import Flask
from .log_config import load_dict_config
from flask.logging import default_handler

app = Flask(__name__)
app.config['ELASTIC_APM'] = {
    'SERVICE_NAME': 'elk-study',
    'SECRET_TOKEN': '',
    'SERVER_URL': os.environ.get("APM_SERVER_PATH", "http://localhost:8200"),
    'ENVIRONMENT': os.environ.get("ENVIRONMENT", "development"),
}

app.logger.removeHandler(default_handler)
apm = ElasticAPM(app)

load_dict_config()
