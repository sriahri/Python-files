animals = []
choice = "start"
while choice != "stop":
    animal = input(" Enter an animal; enter “stop” to quit: ")
    animals.append(animal)

letter = input( "Enter any letter and it will display what animal name which starts with that letter:")
flag = 0
for i in animals:
    if i[0] == letter:
        print(i)
        flag = 1
if not flag:
    print("There is no animal that starts with letter {}".format(letter))

