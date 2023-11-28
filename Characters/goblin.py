from dataclasses import dataclass


@dataclass
class Goblin:
    name: str = "goblin"
    hp: int = 100
    damage: int = 35
