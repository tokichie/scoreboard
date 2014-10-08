from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
import os

if "DATABASE_UR" not in os.environ:
    os.environ["DATABASE_URL"] = "postgres://npqgmqqpvptjop:UeimxyYhifOcl-0h98tf6yh4Qf@ec2-107-21-226-77.compute-1.amazonaws.com:5432/dc6lkrdhlmmc4d";
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host="0.0.0.0", port=port)

