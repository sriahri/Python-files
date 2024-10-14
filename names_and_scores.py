names=[]
ids=[]
score1=[]
score2=[]
score3=[]          
def getStudentInfo(names, ids, score1, score2, score3):
    i = 0
    while i < 4:
        names.append(input("Enter Student "+ str(i+1) + " name: "))
        ids.append(int(input("Enter Student "+ str(i+1) + " id: ")))
        score1.append(float(input("Enter Student "+ str(i+1) + " score1: ")))
        score2.append(float(input("Enter Student "+ str(i+1) + " score2: ")))
        score3.append(float(input("Enter Student "+ str(i+1) + " score3: ")))
        i = i+1
def updateStudentInfo(ids,score1,score2,score3):
        id = int(input("Enter the student id to be updated : "))
        if id in ids:
            pos = ids.index(id)
        else:
            print("ID not found")
            return
        print("")
        score1[pos] = float(input("Enter Score 1: "))
        score2[pos] = float(input("Enter Score 2: "))
        score3[pos] = float(input("Enter Score 3 : "))
        return
def displayStudentInfo(names,ids,score1,score2,score3):
        id = int(input("Enter the student Id : "))
        index = 0
        while index < 4:
            if id == ids[index]:
                    break;
            index = index+1
        if index == 4:
            print("Id not found")
            return
        print("")
        print("Student Name: " + names[index])
        print("Student Id: " + str(ids[index]))
        print("Score 1: " + str(score1[index]))
        print("Score 2: " + str(score2[index]))
        print("Score 3: " + str(score3[index]))
def calculateGrade(ids,score1,score2,score3):
        id = int(input("Enter the student Id : "))
        index = 0
        while index < 4:
                if id == ids[index]:
                     break;
                index = index+1
        if index == 4:
                print("Id not found")
                return
        average = (score1[index] + score2[index] + score3[index]) / 3.0
        grade = " "
        if (average >= 90.0) and (average <= 100.0):
                grade = "A"
        elif (average >= 80.0) and (average <= 89.0):
                grade = "B"
        elif (average >= 70.0) and (average <= 79.0):
                grade = "C"
        elif (average >= 60.0) and (average <= 69.0):
                grade = "D"
        else:
                grade = "F"
        print("Grade : " + grade)
choice = " "
while choice not in ("E","e"):
                print("")
                print("Type P to populate the student information.")
                print("Type U to update student Information.")
                print("Type D to display the student information.")
                print("Type C to calculate the Grade.")
                print("Type E to exit.")
                choice = input("Enter your choice : ")
                if choice not in ("P","p","U","u","D","d","C","c","E","e"):
                            print("Invalid Choice. Try again")
                            continue
                if choice in ("P","p"):
                    getStudentInfo(names,ids,score1,score2,score3)
                elif choice in ("U","u"):
                        updateStudentInfo(ids,score1,score2,score3)
                elif choice in ("D","d"):
                        displayStudentInfo(names,ids,score1,score2,score3)
                elif choice in ("C","c"):
                        calculateGrade(ids,score1,score2,score3)
                else:
                        break