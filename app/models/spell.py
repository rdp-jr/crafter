from . import db

class Spell(db.Model):
    __tablename__ = 'spells'

    id = db.Column(db.Integer, primary_key=True)
    

    def __repr__(self):
        return f'<Spell {self.id}>'