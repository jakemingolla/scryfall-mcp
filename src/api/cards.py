import niquests

from src.api.types import Card, CardId
from src.config.main import config

user_agent = "scryfall-mcp/0.1.0"


async def get_card(card_id: CardId) -> Card:
    async with niquests.AsyncSession() as session:
        response = await session.get(
            f"{config.SCRYFALL_API_BASE_URL}/cards/{card_id}",
            headers={"Accept": "application/json", "User-Agent": user_agent},
        )
        return Card(**response.json())
