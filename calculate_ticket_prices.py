def getContentsAndCalculate():
    file = open("tickets.txt", 'r')
    lines = file.readlines()
    total_cost = 0
    for line in lines:
        tickets, price = map(float, line.split())
        total_cost += tickets * price

    return total_cost


if __name__ == '__main__':
    getContentsAndCalculate()
