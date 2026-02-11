from epl.extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey

class Club(db.Model):
    __tablename__ = 'club'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    players: Mapped[list['Player']] = relationship(back_populates='club')

class Player(db.Model):
    __tablename__ = 'player'
    __table_args__ = {'extend_existing': True} # บรรทัดนี้สำคัญมาก!
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    position: Mapped[str] = mapped_column(String(20), nullable=False)
    goals: Mapped[int] = mapped_column(Integer, default=0, nullable=True)
    clean_sheets: Mapped[int] = mapped_column(Integer, nullable=True)
    squad_no: Mapped[int] = mapped_column(Integer, nullable=True)
    img: Mapped[str] = mapped_column(String(255), nullable=False)
    club_id: Mapped[int] = mapped_column(Integer, ForeignKey('club.id'))

    club: Mapped['Club'] = relationship(back_populates='players')

    def __repr__(self):
        return f'<Player: {self.name}>'