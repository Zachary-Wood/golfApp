from app import db

class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(100))
    total_holes = db.Column(db.Integer)

    holes = db.relationship('Hole', backref='course', cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Course {self.name}>"
