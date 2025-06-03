from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os


from routes.yardage_routes import yardage_bp

app = Flask(__name__)
CORS(app) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///golf.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



from models.course import Course
from models.hole import Hole


db = SQLAlchemy(app)

app.register_blueprint(yardage_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
