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

# ... (โค้ดด้านบนเหมือนเดิม) ...
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # เพิ่ม 3 บรรทัดนี้เข้าไปข้างใน context ด้วยครับ
        from epl.core.routes import core_bp
        from epl.clubs.routes import club_bp
        from epl.players.routes import player_bp

        app.register_blueprint(core_bp, url_prefix='/')
        app.register_blueprint(club_bp, url_prefix='/clubs')
        app.register_blueprint(player_bp, url_prefix='/players')

    return app