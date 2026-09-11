from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def get_db():
    connection = sqlite3.connect("diary.db")
    connection.row_factory = sqlite3.Row
    return connection


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        return "Login received for: " + email

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            return "Passwords do not match!"

        connection = get_db()

        connection.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT UNIQUE, password TEXT)"
        )

        try:
            connection.execute(
                "INSERT INTO users (email, password) VALUES (?, ?)",
                (email, password)
            )
            connection.commit()
        except sqlite3.IntegrityError:
            connection.close()
            return "An account with this email already exists!"

        connection.close()

        return "Account created successfully!"

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
