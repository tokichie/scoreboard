from flask import Flask
import os
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

