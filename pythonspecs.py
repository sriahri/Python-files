def checkAge():
    # We use try except block to check whether the 
    # entered number is integer or not
    try:
        age = int(input('Enter your age between 21 and 99 : '))
        if age >=21 and age <= 99 :
            return 'The age is ',age
        else:
            return 'Age is invalid'
    except Exception:
        return 'Age is invalid'
def driveTruck():
    choice = input('Do you drive a truck ? ').lower()
    if choice == 'y':
        return 'True' # If you want the boolean value remove the quotes
    if choice == 'n':
        return 'False' # If you want the boolean value remove the quotes
def countVowels():
    sentence = input('Enter a senetence : ')
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    c = 0
    for i in sentence:
        if i in vowels:
            c+=1
    return 'The number of vowels are',c
print(*checkAge())
print(driveTruck())
print(*countVowels())