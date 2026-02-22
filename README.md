🐳 Pokeflip

Pokeflip is a FastAPI-based backend service that fetches Pokémon ability data from the public PokeAPI and stores it into a PostgreSQL database.

This project uses:

- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- httpx (async HTTP client)

⚙️ Environment Variables

Create a .env file in project root:

PG_USER=pokeflip_user
PG_PASSWORD=password
PG_DB=pokeflip
PG_HOST=db
PG_PORT=5432

DB_URL=postgresql+asyncpg://pokeflip_user:password@db:5432/pokeflip

🐳 Run with Docker

Build and start containers:

docker compose up --build

🧠 Architecture

This project follows layered architecture:

Schemas → API validation layer

Domains → Business models

Services → Business logic

Repositories → Database access

Models → SQLAlchemy ORM models


Sample Payload:

{
  "raw_id": "ABC1234567890",
  "user_id": "1234567",
  "pokemon_ability_id": 150
}
