def amount_in_words_less_than_ten(amount):
    if amount == '1':
        return 'ONE'
    elif amount == '2':
        return 'TWO'
    elif amount == '3':
        return 'THREE'
    elif amount == '4':
        return 'FOUR'
    elif amount == '5':
        return 'FIVE'
    elif amount == '6':
        return 'SIX'
    elif amount == '7':
        return 'SEVEN'
    elif amount == '8':
        return 'EIGHT'
    elif amount == '9':
        return 'NINE'
    elif amount =='0':
        return 'ZERO'
    
def amount_in_words_between_ten_and_twenty(amount):
    if amount == '10':
        return 'TEN'
    elif amount == '11':
        return 'ELEVEN'
    elif amount == '12':
        return 'TWELVE'
    elif amount == '13':
        return 'THIRTEEN'
    elif amount == '14':
        return 'FOURTEEN'
    elif amount == '15':
        return 'FIFTEEN'
    elif amount == '16':
        return 'SIXTEEN'
    elif amount == '17':
        return 'SEVENTEEN'
    elif amount == '18':
        return 'EIGHTEEN'
    elif amount == '19':
        return 'NINETEEN'
    
def amount_in_words_greater_than_twenty(amount):
    if amount == '2':
        return 'TWENTY'
    elif amount == '3':
        return 'THIRTY'
    elif amount == '4':
        return 'FOURTY'
    elif amount == '5':
        return 'FIFTY'
    elif amount == '6':
        return 'SIXTY'
    elif amount == '7':
        return 'SEVENTY'
    elif amount == '8':
        return 'EIGHTTY'
    elif amount == '9':
        return 'NINTY'
    
file = open("check.txt", "r")
lines = file.readlines()
for i in lines:
    result = ''
    total = i.strip("$").strip("\n").split('.')
    amount = total[0]
    if len(amount)  == 1:
        result += amount_in_words_less_than_ten(amount) + ' '
    elif len(amount) == 2:
        if int(amount) >= 20:
            result += amount_in_words_greater_than_twenty(amount[0]) + ' ' + amount_in_words_less_than_ten(amount[1]) + ' '
        else:
            result += amount_in_words_between_ten_and_twenty(amount) + ' '
    elif len(amount) == 3:
        result += amount_in_words_less_than_ten(amount[0]) + ' HUNDRED '
        if amount[1] == '1':
            result += amount_in_words_between_ten_and_twenty(amount[1:]) + ' '
        else:
            result += amount_in_words_greater_than_twenty(amount[1]) + ' '
            result += amount_in_words_less_than_ten(amount[2]) + ' '
    result += 'DOLLAR AND ' + total[1]  + ' /100'
    print(result)