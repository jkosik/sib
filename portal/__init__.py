from flask import Flask
from portal.config import ProductionConfig, DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    
    with app.app_context():
      db.init_app(app) 
      from portal.main.routes import main
      from portal.model_test.views import model_test
      from portal.target.views import target
      db.create_all()

      app.register_blueprint(main)
      app.register_blueprint(model_test)
      app.register_blueprint(target)

    return app 