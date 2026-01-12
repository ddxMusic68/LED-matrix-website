from flask import Blueprint, render_template, request

views = Blueprint("views", __name__)

@views.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        json = request.json
        print(json)

    return render_template("home.html")