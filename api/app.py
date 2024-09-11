from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
POSTGRES_USER = os.getenv("POSTGRES_USER", "baldwin")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "baldwin_password")
POSTGRES_DB = os.getenv("POSTGRES_DB", "fatal_error_db")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String(80), nullable=True)
    phone_number = db.Column(db.String(20), unique=False, nullable=True)
    it_background = db.Column(db.String(1000), unique=False, nullable=True)
    expectations = db.Column(db.String(1000), unique=False, nullable=True)

    def __repr__(self):
        return f"<Member {self.full_name}>"

@app.route('/test', methods=['GET'])
def test():
    return "hi"

@app.route('/members', methods=['GET'])
def get_members():
    members = Member.query.all()
    return jsonify([{
        'id': member.id,
        'full_name': member.full_name,
        'phone_number': member.phone_number,
        'it_background': member.it_background,
        'expectations': member.expectations
    } for member in members])

@app.route('/members', methods=['POST'])
def create_member():
    data = request.get_json()
    new_member = Member(
        full_name=data.get('full_name'),
        phone_number=data.get('phone_number'),
        it_background=data.get('it_background'),
        expectations=data.get('expectations')
    )
    db.session.add(new_member)
    db.session.commit()
    return jsonify({
        'id': new_member.id,
        'full_name': new_member.full_name,
        'phone_number': new_member.phone_number,
        'it_background': new_member.it_background,
        'expectations': new_member.expectations
    }), 201

@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Not Found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'message': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
