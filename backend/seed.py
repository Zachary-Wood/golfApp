from extensions import db
from models.course import Course
from models.hole import Hole

def seed_data(app):
    with app.app_context():
        # Clear existing data
        Hole.query.delete()
        Course.query.delete()

        # Create Rozella Ford Course
        course = Course(
            name="Rozella Ford Golf Club",
            city="Warsaw",
            state="Indiana",
            country="USA",
            total_holes=18,
            image_url=""
        )
        db.session.add(course)
        db.session.commit()

        # First 2 holes of Rozella Ford
        holes = [
            Hole(
                number=1,
                par=4,
                yardage=380,
                handicap=6,
                tee_lat=41.2231,
                tee_lon=-85.8770,
                green_lat=41.2238,
                green_lon=-85.8755,
                type="straight",
                notes="Fairly open with a slight uphill approach.",
                course_id=course.id
            ),
            Hole(
                number=2,
                par=4,
                yardage=360,
                handicap=12,
                tee_lat=41.2239,
                tee_lon=-85.8754,
                green_lat=41.2247,
                green_lon=-85.8739,
                type="slight dogleg right",
                notes="Shorter hole, aim for center to avoid bunker left.",
                course_id=course.id
            )
        ]

        db.session.add_all(holes)
        db.session.commit()

        print("✅ Seeded Rozella Ford with first 2 holes.")

if __name__ == "__main__":
    seed_data()

