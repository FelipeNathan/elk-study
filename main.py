from flask import Flask
# initialize using environment variables
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)
app.config['ELASTIC_APM'] = {
    'SERVICE_NAME': 'my-service',
    'SECRET_TOKEN': '',
    'SERVER_URL': 'http://localhost:8200',
}

apm = ElasticAPM(app)


@app.route("/home")
def home():
    return "<p>Hello World</p>"

@app.route("/home/me")
def home_me():
    return "<p>Hello Felipe</p>"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)
