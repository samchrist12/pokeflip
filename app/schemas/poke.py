from pydantic import BaseModel, constr

class PokeInput(BaseModel):
    raw_id: constr(pattern=r"^[A-Za-z0-9]{13}$", strict=True)
    user_id: constr(pattern=r"^\d{7}$", strict=True)
    pokemon_ability_id: constr(pattern=r"^\d+$", max_length=5, strict=True)

class PokeResponses(BaseModel):
    raw_id: str
    user_id: str
    returned_entries: list[dict]
    pokemon_list: list[str]