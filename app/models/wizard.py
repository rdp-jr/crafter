from . import db
import wizard_spell

class Wizard(db.Model):
    __tablename__ = 'wizards'
    id = db.Column(db.Integer, primary_key=True)
    wizard_spells = db.relationship('Spell', secondary=wizard_spell, backref=db.backref('wizard_spell', lazy=True))

    def __repr__(self):
        return f'<Wizard {self.id}>'