class Hotel:
    hotel_count = 100

    def __init__(self, hotel_name):
        Hotel.hotel_count += 1
        self.hotel_id = Hotel.hotel_count
        self.hotel_name = hotel_name
        self.rooms = []

    def addNewRoom(self, room):
        self.rooms.append(room)


Hotels = {}


class Room:
    def __init__(self, items):
        self.items = items
        self.price = sum(int(i[1]) for i in self.items)


def addRoomToHotel(hotel):
    limit = 1
    i = 0
    print("Enter items and their values for room")
    items = []
    while i < limit:
        item_name = input("ItemName:")
        if item_name in [i[0] for i in items]:
            print("You have already added this item,Please add another one")
            continue
        if item_name == '':
            print("Item name cannot be empty,add item")
            continue
        item_value = int(input("Item Value in dollars:"))
        items.append((item_name, item_value))
        i += 1
        ansr = ""
        if i >= limit:
            ansr = input("You want to add more ? (y/n) ").lower()
        if ansr == 'y':
            limit += 1
    room = Room(items=items)
    hotel.addNewRoom(room)
    print("Sucessfully Added Rooms")


def displayAll(budget=None):
    output = ""
    available = False
    for id, hotel in Hotels.items():
        room_output = ""
        roomAvailableInHotel = False
        if not budget:
            output += ("\n*Hotel-{0} id-{1}*\n".format(hotel.hotel_name, id))
        for i, room in enumerate(hotel.rooms):
            if budget:
                if budget >= room.price:
                    available = roomAvailableInHotel = True
                    room_output += ("\nRoom{0} price: ${1}\n".format(i+1, room.price) +
                                    "Items available: " + ', '.join(item[0] for item in room.items) + "\n")
            else:
                output += ("\nRoom {0} price: ${1}\n".format(i+1, room.price))
                for item in room.items:
                    output += ("{0}  :   ${1} \n".format(item[0], item[1]))

        if roomAvailableInHotel == True:
            output += ("\n*Hotel {0} id {1}*\n".format(hotel.hotel_name,
                                                       id)) + room_output

    if budget != None:
        if available == False:
            print("Sorry, No Rooms available under ${}..".format(budget))
        else:
            print("Rooms under ${}: ".format(budget))
            print(output)
        return

    print(output)


def main():
    print("------WELCOME------")
    while True:
        print("-"*50)
        print("Select Options 1,2,3 or 4")
        print("1.Add Hotel")
        print("2.Add a room with items and values")
        print("3.Show each room with available items and values")
        print("4.Enter your budget and find rooms")
        print("5.Exit")

        opt_no = input()

        if opt_no == '1':
            hotel_name = input('Enter Hotel Name-')
            hotel = Hotel(hotel_name)
            Hotels[hotel.hotel_id] = hotel
            no_of_rooms = input("Enter Number of rooms to be added : ")
            if no_of_rooms.isdigit():
                no_of_rooms = int(no_of_rooms)
            for i in range(no_of_rooms):
                addRoomToHotel(hotel)

        elif opt_no == '2':
            print("Select hotel- ")
            hotel_ids = list(Hotels.keys())
            print("*"*20)
            print("Serial No\tHotel Id\tHotel Name")
            for i, hotel_id in enumerate(hotel_ids):
                print("{} \t \t{} \t \t{}".format(
                    i, hotel_id, Hotels[hotel_id].hotel_name))
            index = int(input("Enter the Serial No to choose: "))
            hotel = Hotels[hotel_ids[index]]
            addRoomToHotel(hotel)

        elif opt_no == '3':
            displayAll()

        elif opt_no == '4':
            budget = int(input("Enter budget in dollars: $"))
            displayAll(budget)

        elif opt_no == '5':
            exit()

        else:
            print("Invalid Input!! Choose options from 1 to 5")


main()
