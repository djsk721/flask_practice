import flask

app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return 'plz press the like btn !! by Kim 해치웠나 좀 되라'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')