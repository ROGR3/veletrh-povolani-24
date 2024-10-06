from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import random


def is_number(a):
    return type(a) == int or type(a) == float


def is_integer(a):
    return type(a) == int


@dataclass(frozen=True)
class Campaign:
    id: str
    priority: int
    start_date: datetime
    end_date: datetime
    cpm: Optional[float] = None
    gap: Optional[float] = None
    ad_duration_in_sec: Optional[float] = None
    gap_per_network: Optional[dict[str, float]] = None


class Pacer:
    def get_delivery_indicator(self, campaign: Campaign, date: datetime) -> float:
        return 0


class RandomProbabilityGenerator:
    def generate(self) -> float:
        return random.random()
