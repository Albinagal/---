from flask import Flask, render_template, request, redirect, url_for
from DataBase import JsonBase
import main2


app = Flask(__name__)
data = JsonBase("data.json")


@app.route("/")
def home():
    return render_template("1str.html")


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        t_login = request.form["login"]
        t_pas = request.form["pas"]
        check = data.read()
        if t_pas == check.get(t_login):
            return render_template('iPhone 13 Pro Max _ 6.html')
    else:
        return render_template("iPhone 13 Pro Max _ 6.html")


@app.route("/reg", methods=["POST", "GET"])
def reg():
    if request.method == "GET":
        return render_template("2str.html")
    else:
        pass


@app.route("/sign", methods=["POST", "GET"])
def sign():
    if request.method == "GET":
        return render_template("iPhone 13 Pro Max _ 6.html")
    else:
        pass


@app.route("/final", methods=["POST", "GET"])
def final():
    if request.method == "GET":
        return render_template("Final slide.html")
    else:
        return render_template("Final slide.html")


if __name__ == "__main__":
    app.run(debug=True)
