from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
    return "hello world"

@app.route("/abc")
def abc():
    return "This is the ABC route"

@app.route("/<name>")
def greet(name):
    return f"hello, {name}!"

if __name__=="__main__":
    app.run(debug=True)

