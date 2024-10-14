import sys
energy_bill_prior = []
energy_bill_post = []
savings = []
def gatherInfo():
    print('Enter the energy bill Prior to rooftop gardens: ')
    for i in range(1, 13):
        print('Enter the energy bill for month {}: '.format(i))
        try:
            bill = float(input())
            energy_bill_prior.append(bill)
        except:
            print('Please eter the bill in decimal only.')
            sys.exit(0)
    print('Enter the energy bill post to rooftop gardens: ')
    for i in range(1, 13):
        print('Enter the energy bill for month {}: '.format(i))
        try:
            bill = float(input())
            energy_bill_post.append(bill)
        except:
            print('Please eter the bill in decimal only.')
            sys.exit(0)

def savingsAmount():
    for i in range(12):
        savings.append(energy_bill_prior[i] - energy_bill_post[i])
        
def maxAndMinsavings():
    print('The maximum savings occured on {}'.format(savings.index(max(savings))+1))
    print('The minimum savings occured on {}'.format(savings.index(min(savings))+1))
    
def findSaving(month):
    return savings[month-1]

gatherInfo()
savingsAmount()
maxAndMinsavings()
month = int(input('enter the month for which you need the savings: '))
print(findSaving(month))