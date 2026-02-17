# Importamos las clases necesarias
from dataclasses import dataclass, field
from typing import List
from Clases.client import Client 

@dataclass
class HotelManager:# Clase para gestionar las operaciones del hotel, como clientes y reservas
    def __init__(self):# Inicializamos las listas para clientes en habitaciones y reservas en el restaurante
        self.rooms: List[Client] = []
        self.restaurant_reservations: List[Client] = []
    
    def add_client(self, client: Client):# Agregamos un cliente a la lista de clientes en habitaciones
        self.rooms.append(client) 

    def remove_client(self, client: Client):# Eliminamos un cliente de la lista de clientes en habitaciones si existe
        if client in self.rooms:
            self.rooms.remove(client) 

    def add_reservation(self, client: Client) -> List[Client]:# Agregamos una reserva al restaurante, aplicando las reglas para walk-ins y clientes regulares
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