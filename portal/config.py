import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object): 
    SECRET_KEY = '111' 
    DEBUG = True 
    TESTING = False 
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'sib.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/sib.db' 

class ProductionConfig(BaseConfig): 
    DEBUG = False 
    SECRET_KEY = '12345'
 
class DevelopmentConfig(BaseConfig): 
    DEBUG = True 
    TESTING = True 
    SECRET_KEY = '67890' 