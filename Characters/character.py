from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Character:
    name: str
    hp: int = 100
    damage: int = 20
    inventory: Dict[str, int] = field(default_factory=lambda: {"stick": 1, "healing_potion": 3}, compare=False)
