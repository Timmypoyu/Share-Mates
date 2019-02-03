import main
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pizza", methods = ["GET"])
def pizza():

    if request.method == "GET":

        try:

            print("Success")

        except Exception as e:
            return render_template("index.html", text = str(e))

if __name__ == "__main__":
    app.run()