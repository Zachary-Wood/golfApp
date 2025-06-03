from extensions import db
from models.hole import Hole


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(100))
    total_holes = db.Column(db.Integer)
    image_url = db.Column(db.String(255))

    holes = db.relationship(Hole, backref='course', cascade="all, delete-orphan")


    def to_dict(self):
        return {
        "id": self.id,
        "name": self.name,
        "city": self.city,
        "state": self.state,
        "country": self.country,
        "total_holes": self.total_holes,
        "image_url": self.image_url,
        "holes": [hole.to_dict() for hole in self.holes]
    }

