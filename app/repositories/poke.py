from sqlalchemy.ext.asyncio import AsyncSession
from app.models.poke import PokemonAbilityModel
from app.domains.poke import PokemonAbility

class BaseRepository:
    def __init__(self, model, db: AsyncSession):
        self.model = model
        self.db = db

class PokemonAbilityRepository(BaseRepository):

    def __init__(self, db: AsyncSession):
        super().__init__(PokemonAbilityModel, db)
        
    async def bulk_create(self, abilities: list[PokemonAbility]):
        records = [
            a.convert_pokemon_ability_model()
            for a in abilities
        ]
        self.db.add_all(records)
        return records