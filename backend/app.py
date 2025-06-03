from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from extensions import db  
from routes.hole_routes import hole_routes


app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///golf.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)  


from models.course import Course
from models.hole import Hole


app.register_blueprint(hole_routes)


with app.app_context():
    db.create_all()

    if Course.query.count() == 0:
        from seed import seed_data
        seed_data(app)
        print("✅ Auto-seeded database.")
    else:
        print("✅ Database already seeded.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

