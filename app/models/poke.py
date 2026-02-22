from sqlalchemy import Column, String, Integer, Text, JSON
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()

class PokemonAbilityModel(Base):
    __tablename__ = "pokemon_ability"

    id = Column(Integer, primary_key=True, autoincrement=True)
    raw_id = Column(String(13), nullable=False, index=True)
    user_id = Column(String(7), nullable=False, index=True)
    pokemon_ability_id = Column(String(4), nullable=False, index=True)
    effect = Column(Text)
    language = Column(JSON)
    short_effect = Column(Text)