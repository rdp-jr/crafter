from . import db

wizard_spell = db.Table('wizard_spell', 
    db.Column('wizard_id', db.Integer, db.ForeignKey('wizard.id'), primary_key=True), 
    db.Column('spell_id', db.Integer, db.ForeignKey('spell.id'), primary_key=True)
)