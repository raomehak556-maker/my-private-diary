from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>My Private Diary</h1><p>Welcome to your diary!</p>"

if __name__ == "__main__":
    app.run(debug=True)
