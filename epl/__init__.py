import os
from flask import Flask
from epl.extensions import db

def create_app():
    app = Flask(__name__)
    
    # Path สำหรับ PythonAnywhere
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/THIPOK/flask-premier-league/epl.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = b'hguyfdrerdfguhiophgytrt'

    db.init_app(app)

    with app.app_context():
        # Import ภายในเพื่อป้องกัน Error ตารางซ้ำ
        from epl.core.routes import core_bp
        from epl.clubs.routes import club_bp
        from epl.players.routes import player_bp
        import epl.models 

        app.register_blueprint(core_bp, url_prefix='/')
        app.register_blueprint(club_bp, url_prefix='/clubs')
        app.register_blueprint(player_bp, url_prefix='/players')

    return app