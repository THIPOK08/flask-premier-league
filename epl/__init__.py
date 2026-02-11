import os
from flask import Flask
from epl.extensions import db, migrate
from epl.core.routes import core_bp
from epl.clubs.routes import club_bp
from epl.players.routes import player_bp

def create_app():
    app = Flask(__name__)
    
    # 1. ตั้งค่าฐานข้อมูลเป็น SQLite (แก้ตัวสะกด SQLALCHEMY ให้ถูกแล้ว)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/THIPOK/flask-premier-league/epl.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = b'hguyfdrerdfguhiophgytrt'

    # 2. เริ่มต้น Database
    db.init_app(app)
    migrate.init_app(app, db)

    # 3. การ Register Blueprint ต้องทำภายใน App Context เพื่อป้องกัน Error ตารางซ้ำ
    with app.app_context():
        # จดทะเบียนเส้นทางต่างๆ
        app.register_blueprint(core_bp, url_prefix='/')
        app.register_blueprint(club_bp, url_prefix='/clubs')
        app.register_blueprint(player_bp, url_prefix='/players')

    return app