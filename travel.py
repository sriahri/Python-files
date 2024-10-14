class Traveler:
    def __init__(self,name, country,age,cfrom):
        self.name = name
        self.country = country
        self.age = age
        self.cfrom = cfrom
class TravelAgency:
    def __init__(self,tlist):
        self.tlist = tlist
    def countTravellers(self,c):
        travellers = 0
        for i in self.tlist:
            for j in i.country:
                if j == c:
                    travellers += 1
        return travellers
    def maxTravelled(self):
        maxi = 0
        index = 0
        for i in self.tlist:
            if len(i.country) > maxi:
                maxi = len(i.country)
                index = i
        return index.name
xlist = []
for _ in range(int(input())):
    name = input()
    l = []
    for i in range(int(input)):
        l.append(input())
    age = int(input())
    cfrom = input()
    t = Traveler(name,l,age,cfrom)
    xlist.append(t)
obj = TravelAgency(xlist)
countryname = input()
print(obj.countTravellers(countryname))
print(obj.maxTravelled())