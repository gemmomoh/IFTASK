from app import db


class student(db.Model):
    __tablename__='student'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False, unique=True)
    code=db.Column(db.String(10), nullable=False, unique=True)

    def __repr__(self):
        return f'<student>{self.name}'