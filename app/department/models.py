from app import db


class Department(db.Model):
    __tablename__='Department'
    id=db.Column(db.Integer, primary_key=True)
    faculty_id=db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)
    name=db.Column(db.String(50), nullable=False, unique=True)
    code=db.Column(db.String(10), nullable=False, unique=True)

    def __repr__(self):
        return f'<Department>{self.name}'