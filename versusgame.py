from random import randint
class DiceShaker:
    def __init__(self,number):
        self.number = number
class VersusGame:
    def __init__(self,args):
        self.num = args.number
        self.player = []
        self.computer = []
    def roll():
        for i in range(self.num):
            x = randint()%self.num + 1
            self.computer.append(x)
            x = randint()%self.num + 1
            self.player.append(x)
        print('Computer rolled :',computer)
        print('Player rolled :',player)
        if float(getScore()) > self.num/2:
            print('You Win! You had',getScore/self.num
    def getGameCount():
        return self.num
    def getScore():
        count = 0
        for i in range(self.num):
            if self.player[i] >= self.computer[i]:
                count += 1
        return count
ds = DiceShaker(4)
g = VersusGame(ds)
g.roll()
