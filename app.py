from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return ("Hello")

@app.route("/show/")
def show():
    return ("Show me the money")

@app.route("/add/")
def add():
    return ("add function")


if __name__ == "__main__":
    app.run(debug=True)