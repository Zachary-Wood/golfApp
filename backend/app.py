from flask import Flask, jsonify
from flask_cors import CORS

from routes.yardage_routes import yardage_bp

app = Flask(__name__)
CORS(app) 

app.register_blueprint(yardage_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
