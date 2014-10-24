from main import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bat_first_team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    bat_last_team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    win_team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    
    def __init__(self, bf_id, bl_id, start_time):
        self.bat_first_team_id = bf_id
        self.bat_last_team_id = bl_id
        self.start_time = start_time

    def __repr__(self):
        return '<Game %r>' % self.id

