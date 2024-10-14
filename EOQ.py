import math,sys
def get_valid_input(s):
    try:
        x = float(s)
        return x
    except:
        return -1
def EOQ(d, h, s):
    if d > 0 and h > 0 and s > 0:
        return math.sqrt((2*d*s)/h)
    return -1
while(1):
    demand = input('Please input a numeric value for Demand : ')
    demand = get_valid_input(demand)
    if demand == -1:
        print('Non numeric value entered')
        continue
    Holding_cost = input('Please input a numeric value for Holding Cost : ')
    Holding_cost = get_valid_input(Holding_cost)
    if Holding_cost == -1:
        print('Non numeric value entered')
        continue
    ordering_cost = input('Please input a numeric value for Ordering Cost : ')
    ordering_cost = get_valid_input(ordering_cost)
    if ordering_cost == -1:
        print('Non numeric value entered')
        continue
    result = EOQ(demand,Holding_cost,ordering_cost)
    if result != -1:
        print('The EOQ, for a demand of',demand,'holding cost of',Holding_cost,'and ordering cost of',ordering_cost,'is','%.2f'%result)
    else:
        print('One of the inputs is Zero or negative')
    choice = input('Compute EOQ again? (Y/N)').upper()
    if choice == 'N':
        break