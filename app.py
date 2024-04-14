from appmap.flask import AppmapFlask
from flask import Flask, request_finished, request_started

app = Flask(__name__)
AppmapFlask().init_app(app)

app.config["SECRET"] = "1231231423"


def get_message():
    return "Please work"


@app.route("/")
def index():
    return get_message()


@app.route("/test")
def num2():
    return "I have not lost my mind"


if __name__ == "__main__":
    app.run()
