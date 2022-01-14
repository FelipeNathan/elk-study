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
    except ZeroDivisionError:
        extra = {"tags": {"good_at_math": "false"}}
        app.logger.error("Math division", exc_info=True, extra=extra)

    return "<p>error captured</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
