import logging
import asyncio

from loguru import logger

from app.domains.poke import PokemonAbility
from app.schemas.poke import PokeInput, PokeResponses
from app.repositories.poke import PokemonAbilityRepository
from app.db.session import get_db_session

import httpx


class PokemonAbilityService:
    
    def __init__(self, client: httpx.AsyncClient):
        self.client = client

    async def process_pokemon_ability(
            self,
            poke: PokeInput
    ):
        self.poke = poke

        logger.info(f"Call pokeapi with ability_id {self.poke.pokemon_ability_id}")
        response = await self.client.get(
            f"https://pokeapi.co/api/v2/ability/{self.poke.pokemon_ability_id}"
        )

        if response.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail=f"Pokemon Ability with ability_id {self.poke.pokemon_ability_id} not found"
            )
        
        data = response.json()
        effect_entries = data['effect_entries']
        pokemon_list = [p['pokemon']['name'] for p in data['pokemon']]
        abilities = []
        for effect in effect_entries:
            abi = PokemonAbility(
                raw_id = self.poke.raw_id,
                user_id = self.poke.user_id,
                pokemon_ability_id = self.poke.pokemon_ability_id,
                effect = effect['effect'],
                language = effect['language'],
                short_effect = effect['short_effect']
            )
            abilities.append(abi)

        async with get_db_session() as session:
            poke_repo = PokemonAbilityRepository(session)
            try:

                logger.info(f"Bulk store Pokemon Ability info to database")
                await poke_repo.bulk_create(
                    abilities = abilities
                )

                logger.info(f"Finished task. Storing the results and updating to db...")
                
                await session.commit()
            except Exception as e:
                await session.rollback()
                logger.error("Error when storing data to DB")
                raise Exception(f"Failed to update : {e}") from e
        
        rsp = PokeResponses(
            raw_id = poke.raw_id,
            user_id = poke.user_id,
            returned_entries = effect_entries,
            pokemon_list = pokemon_list
        )

        return rsp