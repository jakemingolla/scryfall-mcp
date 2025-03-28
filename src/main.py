import asyncio

from src.api.cards import get_card
from src.api.types import CardId


async def main():
    card = await get_card(CardId("56ebc372-aabd-4174-a943-c7bf59e5028d"))
    print(card.name)


if __name__ == "__main__":
    asyncio.run(main())
