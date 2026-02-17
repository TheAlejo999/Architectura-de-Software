# Imports de las clases necesarias para el programa
from dataclasses import dataclass, field
from typing import List

# Clase para representar a un cliente del hotel
@dataclass
class Client:
    id: int
    name: str
    age: int
    email: str
    isWalkIn: bool = False
