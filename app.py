from flask import Flask, request, jsonify
from models import db, Sample, Experiment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample_tracking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/samples', methods=['GET'])
def get_samples():
    samples = Sample.query.all()
    return jsonify([s.to_dict() for s in samples])

@app.route('/samples', methods=['POST'])
def add_sample():
    data = request.json
    sample = Sample(name=data['name'], description=data.get('description', ''))
    db.session.add(sample)
    db.session.commit()
    return jsonify(sample.to_dict()), 201

@app.route('/experiments', methods=['GET'])
def get_experiments():
    experiments = Experiment.query.all()
    return jsonify([e.to_dict() for e in experiments])

@app.route('/experiments', methods=['POST'])
def add_experiment():
    data = request.json
    experiment = Experiment(name=data['name'], result=data.get('result', ''))
    db.session.add(experiment)
    db.session.commit()
    return jsonify(experiment.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
