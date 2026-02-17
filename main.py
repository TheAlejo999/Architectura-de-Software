from Clases.client import Client
from Clases.hotelManager import HotelManager

def main():
    print("Hello from py-hotel-example!")
    
    hotel_manager = HotelManager()

    client1 = Client(id=1, name="John Doe", age=30, email="john.doe@example.com", isWalkIn=False)
    client2 = Client(id=2, name="Jane Smith", age=25, email="jane.smith@example.com", isWalkIn=False)
    client3 = Client(id=3, name="Bob Johnson", age=40, email="bob.johnson@example.com", isWalkIn=False)
    client4 = Client(id=4, name="Alice Brown", age=35, email="alice.brown@example.com", isWalkIn=False)
    client5 = Client(id=5, name="Charlie Davis", age=28, email="charlie.davis@example.com", isWalkIn=False)
    client6 = Client(id=6, name="Eve Wilson", age=22, email="eve.wilson@example.com", isWalkIn=True)
    client7 = Client(id=7, name="Frank Miller", age=45, email="frank.miller@example.com", isWalkIn=True)
    client8 = Client(id=8, name="Grace Lee", age=32, email="grace.lee@example.com", isWalkIn=True)

    for c in [client1, client2, client3, client4, client5]:
        hotel_manager.add_client(c)

    print("\nCurrent clients in the hotel:")
    for client in hotel_manager.rooms:
        print(client)

    print("\n")
    hotel_manager.remove_client(client1)
    print("Clients after removing one:")
    for client in hotel_manager.rooms:
        print(client)

    print("\n")
    hotel_manager.add_reservation(client1) 
    hotel_manager.add_reservation(client2) 
    hotel_manager.add_reservation(client3) 
    hotel_manager.add_reservation(client4) 
    hotel_manager.add_reservation(client6) 
    hotel_manager.add_reservation(client7) 
    hotel_manager.add_reservation(client5) 
    hotel_manager.add_reservation(client8) 

if __name__ == "__main__":
    main()