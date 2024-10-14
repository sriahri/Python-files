class Passenger:
    def __init__(self,passengerName, passengerAge, distanceTravelled):
        self.passengerName = passengerName
        self.passengerAge = passengerAge
        self.distanceTravelled = distanceTravelled
    @classmethod
    def calculateTicketFare(cls,passengersList,farePerKilometer):
        total_fare = 0
        fare = 0
        for i in passengersList:
            fare = i.distanceTravelled * farePerKilometer
            if i.passengerAge >= 60 or i.passengerAge < 12:
                total_fare += fare
            elif i.passengerAge >= 21 and i.passengerAge <= 59 :
                total_fare += fare + fare * 0.12
            elif i.passengerAge >= 12 and i.passengerAge <= 20 :
                total_fare += fare +fare * 0.10
            print(fare)
            print(total_fare)
        print(total_fare)
    @classmethod
    def countSeniorJuniorPassengers(cls,passengersList):
        count = 0
        for i in passengersList:
            if i.passengerAge >= 60 or i.passengerAge < 12:
                count += 1
        print(count)

n = int(input())
passengerList = []
for i in range(n):
    name = input()
    age = int(input())
    distance = int(input())
    p = Passenger(name,age,distance)
    passengerList.append(p)
fare = int(input())
Passenger.calculateTicketFare(passengerList,fare)
Passenger.countSeniorJuniorPassengers(passengerList)