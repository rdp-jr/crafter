from . import db

class Contact_info(db.Model):
    __tablename__ = 'contact_infos'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

    def __repr__(self):
        return f'<Contact_info {self.id}>'