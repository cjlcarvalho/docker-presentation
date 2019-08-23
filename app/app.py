from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps

app = Flask(__name__)

app.secret_key = "minha chavezinha top"


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Você precisa estar logado.")
            return redirect(url_for("login"))

    return wrap


@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["username"] != "admin" or request.form["password"] != "admin":
            error = "Credenciais inválidas. Tente novamente."
        else:
            session["logged_in"] = True
            flash("Você acabou de logar!")
            return redirect(url_for("index"))
    return render_template("login.html", error=error)


@app.route("/logout")
@login_required
def logout():
    session.pop("logged_in", None)
    flash("Você saiu de sua conta!")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")
