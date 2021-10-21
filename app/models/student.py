from . import db

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    contact_info = db.relationship('Contact_info', backref='student', lazy=True, uselist=False)
    classes = db.relationship('Class', backref='student', lazy=True)

    def __repr__(self):
        return f'<Student {self.id}>'