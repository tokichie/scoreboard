from main import db

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

