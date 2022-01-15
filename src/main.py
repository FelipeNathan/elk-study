import elasticapm

from config.app_config import app, apm


@app.route("/home")
def home():
    app.logger.info("Calling /home - Lets goooooo")
    return "<p>Hello World</p>"


@app.route("/home/me")
def home_me():
    return "<p>Hello Felipe</p>"


@app.route("/error/capture/exception")
def handle_exception():
    try:
        1 / 0
    except ZeroDivisionError:
        apm.capture_exception()

    return "<p>error captured</p>"


@app.route("/error/capture/message")
def handle_message():
    apm.capture_message("handling error")

    return "<p>error captured</p>"


@app.route("/error/capture/extra")
def handle_extra():
    try:
        1 / 0
    except ZeroDivisionError as e:
        extra = {"extra": {"exception": e.__str__()}}
        app.logger.error("Math division", extra=extra, exc_info=True)

    return "<p>error captured</p>"


@app.route("/error/capture/should/<throw>")
def not_capture_error(throw="true"):
    if throw == "true":
        1 / 0
    else:
        return "<p>not throwing exception</p>"


@app.route("/events")
@app.route("/events/<event_name>")
def events(event_name="no.event.name"):
    elasticapm.set_transaction_name(event_name)
    return f"<p>{event_name}</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
