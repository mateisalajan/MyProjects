from dataclasses import dataclass


@dataclass
class Golem:
    name: str = "golem"
    hp: int = 250
    damage: int = 100
