from flask import Flask, redirect, url_for, render_template, request, session
import os

app = Flask(__name__)

app.config["UPLOADS"] ="#path"

app.secret_key = "test123"
@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if request.files:
            file = request.files["file1"]
            file.save(os.path.join(app.config["UPLOADS"], file.filename))
            print(file)
            return redirect(url_for("dashboard"))
    return render_template("upload.html")
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():


        dir1 = os.listdir("#path")
        return render_template("files.html", dirs=dir1)
