from portal import db

class Assets(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    ipset = db.Column(db.String(255)) 
     
    def __init__(self, ipset): 
        self.ipset = ipset 
 
    def __repr__(self): 
        return '<Assets %d>'.format(self.id)