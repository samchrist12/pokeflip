from fastapi import FastAPI
from fastapi import HTTPException
from app.schemas.poke import PokeInput, PokeResponses
from app.domains.poke import PokemonAbility
from app.repositories.poke import PokemonAbilityRepository
from app.services.poke import PokemonAbilityService
from app.db.session import get_db_session
from fastapi import status
from loguru import logger
import httpx

app = FastAPI()

@app.on_event("startup")
async def startup():
    app.state.client = httpx.AsyncClient(timeout=10.0)

@app.on_event("shutdown")
async def shutdown():
    await app.state.client.aclose()

@app.get("/")
async def welcome():
    return "{'message': 'welcome'}"

@app.get("/health")
async def healthcheck():
    return "{'message': 'OK'}"

@app.post("/poke")
async def create_poke(poke: PokeInput):
    svc = PokemonAbilityService(app.state.client)
    rsp = await svc.process_pokemon_ability(poke)

    return rsp