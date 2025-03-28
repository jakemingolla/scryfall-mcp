import uuid
from typing import Dict, List, NewType, Optional

from pydantic import BaseModel, Field

CardId = NewType("CardId", uuid.UUID)
ArtistId = NewType("ArtistId", uuid.UUID)


class CardFace(BaseModel):
    artist: Optional[str] = None
    artist_id: Optional[ArtistId] = None
    cmc: Optional[float] = None
    color_indicator: Optional[List[str]] = None
    colors: Optional[List[str]] = None
    defense: Optional[str] = None
    flavor_text: Optional[str] = None
    illustration_id: Optional[uuid.UUID] = None
    image_uris: Optional[Dict[str, str]] = None
    layout: Optional[str] = None
    loyalty: Optional[str] = None
    mana_cost: str
    name: str
    oracle_id: Optional[uuid.UUID] = None
    oracle_text: Optional[str] = None
    power: Optional[str] = None
    toughness: Optional[str] = None
    type_line: Optional[str] = None
    watermark: Optional[str] = None


class RelatedCard(BaseModel):
    id: CardId
    object: str = "related_card"
    component: str
    name: str
    type_line: str
    uri: str


class Card(BaseModel):
    # Core Fields
    arena_id: Optional[int] = None
    id: CardId
    lang: str
    mtgo_id: Optional[int] = None
    mtgo_foil_id: Optional[int] = None
    multiverse_ids: Optional[List[int]] = None
    tcgplayer_id: Optional[int] = None
    tcgplayer_etched_id: Optional[int] = None
    cardmarket_id: Optional[int] = None
    object: str = "card"
    layout: str
    oracle_id: Optional[uuid.UUID] = None

    # Gameplay Fields
    all_parts: Optional[List[RelatedCard]] = None
    card_faces: Optional[List[CardFace]] = None
    cmc: float = Field(description="Mana value")
    color_identity: List[str]
    color_indicator: Optional[List[str]] = None
    colors: Optional[List[str]] = None
    defense: Optional[str] = None
    edhrec_rank: Optional[int] = None
    hand_modifier: Optional[str] = None
    keywords: List[str] = Field(default_factory=list)
    legalities: Dict[str, str]
    life_modifier: Optional[str] = None
    loyalty: Optional[str] = None
    mana_cost: Optional[str] = None
    name: str
    oracle_text: Optional[str] = None
    power: Optional[str] = None
    produced_mana: Optional[List[str]] = None
    reserved: bool
    toughness: Optional[str] = None
    type_line: str

    # Print Fields
    artist: Optional[str] = None
    artist_id: Optional[ArtistId] = None
    attraction_lights: Optional[List[int]] = None
    booster: bool
    border_color: str
    card_back_id: Optional[uuid.UUID] = None
    collector_number: str
    content_warning: Optional[bool] = None
    digital: bool
    finishes: List[str]
    flavor_name: Optional[str] = None
    flavor_text: Optional[str] = None
    frame_effects: Optional[List[str]] = None
    frame: str
    full_art: bool
    games: List[str]
    highres_image: bool
    illustration_id: Optional[uuid.UUID] = None
    image_status: str
    image_uris: Optional[Dict[str, str]] = None
    oversized: bool
    prices: Dict[str, Optional[str]]
    printed_name: Optional[str] = None
    printed_text: Optional[str] = None
    printed_type_line: Optional[str] = None
    promo: bool
    promo_types: Optional[List[str]] = None
    purchase_uris: Optional[Dict[str, str]] = None
    rarity: str
    related_uris: Dict[str, str]
    released_at: str
    reprint: bool
    scryfall_set_uri: str
    security_stamp: Optional[str] = None
    set_name: str
    set_search_uri: str
    set_type: str
    set_uri: str
    set: str
    set_id: uuid.UUID
    story_spotlight: bool
    textless: bool
    variation: bool
    variation_of: Optional[uuid.UUID] = None
    watermark: Optional[str] = None
