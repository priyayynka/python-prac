class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"the name of the train is {self.name}")
        print(f"the no. of seats in the train are {self.seats}")

    def getFare(self):
        print(f"the fare is {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked and seat no. is {self.seats}")
            self.seats -= 1
        else:
            print("train is full!")

intercity = Train("Intercity Express", 90, 300)
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()
intercity.getFare()
