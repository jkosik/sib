from portal import db
from flask_wtf import FlaskForm 
from wtforms import StringField, DecimalField, SelectField 

class TargetSet(db.Model): 
    __tablename__ = 'targetset'
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(255)) 
    target = db.relationship('Target', backref='ts', lazy='dynamic') # to establish .targetset attribute on child Target which will refer to parent TargetSet as target.targetset (backref can not be the same as the child column name)
    
    def __init__(self, name): 
        self.name = name 
 
    def __repr__(self): 
        #return '<Target Sets %d>'.format(self.id)
        return f'{self.name}'
     
    def __str__(self):
        return f'{self.name}'    

class Target(db.Model): 
    __tablename__ = 'target'
    id = db.Column(db.Integer, primary_key=True) 
    target = db.Column(db.String(255)) 
    targetset_id = db.Column(db.Integer, db.ForeignKey('targetset.id')) 
     
    def __init__(self, target, targetset_id): 
        self.target = target
        self.targetset_id = targetset_id 
 
    def __repr__(self): 
        #return '<Targets %d>'.format(self.id)
        return f'{self.targetset_id}: {self.target}'

    def __str__(self):
        return f'{self.target}'
 
class TargetSetForm(FlaskForm): 
    name = StringField('Name') 

