import os
from logging.config import dictConfig

from elasticapm.contrib.flask import ElasticAPM
from flask import Flask

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
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

app = Flask(__name__)
app.config['ELASTIC_APM'] = {
    'SERVICE_NAME': 'elk-study',
    'SECRET_TOKEN': '',
    'SERVER_URL': os.environ.get("APM_SERVER_PATH", "http://localhost:8200"),
}

apm = ElasticAPM(app)


@app.route("/home")
def home():
    app.logger.info("Calling /home - Lets goooooo")
    return "<p>Hello World</p>"


@app.route("/home/me")
def home_me():
    return "<p>Hello Felipe</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
