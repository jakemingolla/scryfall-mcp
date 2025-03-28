import pytest

from src.api.cards import get_card
from src.api.types import CardId


@pytest.mark.asyncio
async def test_happy_path_get_card():
    card_id = CardId("56ebc372-aabd-4174-a943-c7bf59e5028d")
    card = await get_card(card_id)
    assert card is not None
    assert str(card.id) == card_id
    assert card.name == "Phantom Nishoba"
    assert card.type_line == "Creature — Cat Beast Spirit"
