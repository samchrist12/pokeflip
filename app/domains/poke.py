from dataclasses import dataclass

from app.models.poke import PokemonAbilityModel

@dataclass
class PokemonAbility:
    raw_id: str
    user_id: str
    pokemon_ability_id: str
    effect: str
    language: dict
    short_effect: str

    def convert_pokemon_ability_model(self):
        return PokemonAbilityModel(
            raw_id=self.raw_id,
            user_id=self.user_id,
            pokemon_ability_id=self.pokemon_ability_id,
            effect=self.effect,
            language=self.language,
            short_effect=self.short_effect,
        )