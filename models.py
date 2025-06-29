from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'description': self.description}

class Experiment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    result = db.Column(db.String(100))

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'result': self.result}
