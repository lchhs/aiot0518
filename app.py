from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return ("Hello")

@app.route("/index2/")
def index2():
    return "<h2>This is my IoT Web </h2>"

@app.route("/show/")
def show():
    return ("Show me the money")

@app.route("/add/")
def add():
    return ("add function")


if __name__ == "__main__":
    app.run(debug=True)