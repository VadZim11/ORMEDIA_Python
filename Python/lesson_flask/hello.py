from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World<h1>"

@app.route("/hello")
def hello():
    return f"<h2>Hello, {request.args}<h2>" 

if __name__ == "__main__":  
    app.run()