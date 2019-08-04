from app import db
 
class Alarm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(255))
    name = db.Column(db.String(255))
 
    def __init__(self, name, time):
        self.name = name
        self.time = time
 
    def __repr__(self):
        return '<Alarm %d>' % self.id