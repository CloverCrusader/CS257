import flask

app = flask.Flask(__name__)

@app.route('/')
def welcome():
    message = "Welcome to My Example Webpage."
    message = message + " This text was produced by concatenating strings in Python!"
    return flask.render_template("homepage.html", someText = message)

if __name__ == '__main__':
    my_port = 5123
    app.run(host='0.0.0.0', port = my_port)