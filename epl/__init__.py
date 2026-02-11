import os
from flask import Flask
from epl.extensions import db, migrate
from epl.core.routes import core_bp
from epl.clubs.routes import club_bp
from epl.players.routes import player_bp


def create_app():
  app = Flask(__name__)
  # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql12816709:36I6sMQTUz@sql12.freesqldatabase.com:3306/sql12816709'
  # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/epl_s02_db'
  # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/epl_s02_db'
  # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://epl_postgresql_db_user:olbj7CSlns1K6fE7EOEfppm3pyqueRK2@dpg-d65kn594tr6s73fsn1fg-a.oregon-postgres.render.com/epl_postgresql_db'
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/THIPOK/flask-premier-league/epl.db'
  # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  # postgresql://epl_db_2ezk_user:20nPxFMn0I5WrMlyjIDBme2ShC2weHJ9@dpg-d65lcvtum26s73b7o6a0-a.oregon-postgres.render.com/epl_db_2ezk
  app.secret_key = b'hguyfdrerdfguhiophgytrt'
  
  db.init_app(app)
  migrate.init_app(app, db)

  app.register_blueprint(core_bp, url_prefix='/')
  app.register_blueprint(club_bp, url_prefix='/clubs')
  app.register_blueprint(player_bp, url_prefix='/players')

  return app