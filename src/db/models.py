import atexit
import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey, text
from db.connection import engine
from werkzeug.security import generate_password_hash,  check_password_hash

class Base(DeclarativeBase):

    @property    
    def id_dict(self):
        return {"id": self.id}



class Advertisements(Base):
    __tablename__ = "advertisements"
    
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    
    owner: Mapped[str] = mapped_column(
        String, 
        nullable=True
)
    created_at: Mapped[datetime.datetime] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
)
    updated_at: Mapped[datetime.datetime] = mapped_column(
        onupdate=text("TIMEZONE('utc', now())"), nullable=True
)
    
    
    @property 
    def dict(self):
        payload = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at,
            "owner": self.owner,
            "updated_at": self.updated_at
            }
        return payload

Base.metadata.create_all(bind=engine)
atexit.register(engine.dispose)