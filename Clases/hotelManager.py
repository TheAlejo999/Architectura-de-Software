# Importamos las clases necesarias
from dataclasses import dataclass, field
from typing import List
from Clases.client import Client 

@dataclass
class HotelManager:
    def __init__(self):
        self.rooms: List[Client] = []
        self.restaurant_reservations: List[Client] = []
    
    def add_client(self, client: Client):
        self.rooms.append(client) 

    def remove_client(self, client: Client):
        if client in self.rooms:
            self.rooms.remove(client) 

    def add_reservation(self, client: Client) -> List[Client]:
        total_reservations = len(self.restaurant_reservations) 
        walk_ins_count = sum(1 for c in self.restaurant_reservations if c.isWalkIn) 
        regulars_count = total_reservations - walk_ins_count 

        if client.isWalkIn:
            if total_reservations < 6 and walk_ins_count < 2:
                print(f"Adding walk-in reservation for client: {client}") 
                self.restaurant_reservations.append(client) 
            else:
                print(f"No available slots for walk-in reservations for client: {client}") 
        else:
            if total_reservations < 6 and regulars_count < 4:
                print(f"Adding reservation for client: {client}") 
                self.restaurant_reservations.append(client) 
            else:
                print(f"No available slots for reservations for client: {client}") 

        return self.restaurant_reservations 