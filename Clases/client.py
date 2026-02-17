from dataclasses import dataclass, field
from typing import List

@dataclass
class Client:
    id: int
    name: str
    age: int
    email: str
    isWalkIn: bool = False
