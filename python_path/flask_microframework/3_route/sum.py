import flask
app = flask.Flask(__name__)


@app.route("/sum/<a>/<b>")
def sum(a, b):
    result=str(int(a)+int(b))
    return result


if __name__ == '__main__':
    app.debug = True
    app.run()
