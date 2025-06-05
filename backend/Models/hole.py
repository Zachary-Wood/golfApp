

from extensions import db

class Hole(db.Model):
    __tablename__ = 'holes'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    par = db.Column(db.Integer, nullable=False)
    yardage = db.Column(db.Integer, nullable=False)
    handicap = db.Column(db.Integer)
    type = db.Column(db.String(50))
    notes = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    tee_lat = db.Column(db.Float)
    tee_lon = db.Column(db.Float)
    green_lat = db.Column(db.Float)
    green_lon = db.Column(db.Float)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)

    def __repr__(self):
        return f"<Hole {self.number} - {self.yardage} yds>"

    def to_dict(self):
        return {
            "id": self.id,
            "number": self.number,
            "par": self.par,
            "yardage": self.yardage,
            "handicap": self.handicap,
            "type": self.type,
            "notes": self.notes,
            "image_url": self.image_url,
            "tee": {
                "lat": self.tee_lat,
                "lon": self.tee_lon
            },
            "green": {
                "lat": self.green_lat,
                "lon": self.green_lon
            }
        }