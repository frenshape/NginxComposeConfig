# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>This is app F1</h1>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
