from flask import Flask, render_templates
app=Flask(__name__)
@app.route("/")
def hello_world():
    return render_templates("index.html", title="Hello")

@app.route("/home")
def home():
    return render_templates("home.html")