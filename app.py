import main
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/food")
def food():
    return render_template("food.html")

@app.route("/pizza", methods = ["POST"])
def pizza():

    if request.method == "POST":

    	print(request.form["amount"])

    return render_template("success.html")

if __name__ == "__main__":
    app.run()