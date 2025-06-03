from extensions import db

class Hole(db.Model):
    __tablename__ = 'holes'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    par = db.Column(db.Integer, nullable=False)
    yardage = db.Column(db.Integer, nullable=False)
    handicap = db.Column(db.Integer)

    tee_lat = db.Column(db.Float)
    tee_lon = db.Column(db.Float)
    green_lat = db.Column(db.Float)
    green_lon = db.Column(db.Float)

    type = db.Column(db.String(50))
    notes = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    elevation_change = db.Column(db.Float)

    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)

    def __repr__(self):
        return f"<Hole {self.number} - {self.yardage} yds, Par {self.par}>"
