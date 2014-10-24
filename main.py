# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template, url_for, request, redirect, flash
from flask.ext.sqlalchemy import SQLAlchemy
import os

if "DATABASE_UR" not in os.environ:
    #os.environ["DATABASE_URL"] = "postgres://npqgmqqpvptjop:UeimxyYhifOcl-0h98tf6yh4Qf@ec2-107-21-226-77.compute-1.amazonaws.com:5432/dc6lkrdhlmmc4d";
    os.environ["DATABASE_URL"] = "postgres://postgres:to02yu11@localhost:5432/postgres"

app = Flask(__name__)
app.secret_key = 'secretkey'
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
db = SQLAlchemy(app)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    #games = db.relationship('Game')#, backref='team', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Team %r>' % self.id

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bat_first_team_id = db.Column(db.Integer)#, db.ForeignKey('team.id'))
    bat_last_team_id = db.Column(db.Integer)#, db.ForeignKey('team.id'))
    win_team_id = db.Column(db.Integer)#, db.ForeignKey('team.id'))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    scores = db.relationship('Score')
    
    def __init__(self, bf_id, bl_id, start_time):
        self.bat_first_team_id = bf_id
        self.bat_last_team_id = bl_id
        self.start_time = start_time

    def __repr__(self):
        return '<Game %r>' % self.id

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    inning = db.Column(db.Integer)
    score = db.Column(db.Integer)

    def __init__(self, gameid, teamid, inning, score):
        self.game_id = gameid
        self.team_id = teamid
        self.inning = inning
        self.score = score

    def __repr__(self):
        return '<Score %r>' % self.id


@app.route("/")
def index():
    games = getGames()
    print games
    return render_template('index.html', games=games)

@app.route("/add_game", methods=["GET"])
def add_game():
    return render_template('add_game.html')

@app.route("/add_team", methods=["GET"])
def add_team():
    return render_template('add_team.html')

@app.route("/makegame", methods=["GET"])
def make_game():
    return '<%r %r>' % (request.args.get('bat_first'), request.args.get('bat_last'))
    return "aa"

@app.route("/make_team", methods=["GET"])
def make_team():
    name = request.args.get('team_name')
    if name == '':
        flash(u'チーム名を入力してください')
        return redirect(url_for('index'))
    return "aa"

def getGames():
    games = Game.query.all()
    teams = Team.query.all()
    res = []
    for game in games:
        print game.id, game.scores
        bft = Team.query.filter_by(id=game.bat_first_team_id).first()
        blt = Team.query.filter_by(id=game.bat_last_team_id).first()
        res.append( (bft, blt) )
    return res

if __name__ == "__main__":
    app.run(debug=True)
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host="0.0.0.0", port=port)

