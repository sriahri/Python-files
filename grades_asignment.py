import random
def main():
    size = 11
    lst_stu_names = ["Vernon", "Domenic", "Michael", "Celena",
                    "Odis", "Rufus", "Rose", "Cheryll",
                     "Mignon", "Monte", "Ralph"]

    lst_stu_grades = [""] * size

    for i in range(size):
         lst_stu_grades[i] = random.choice(["A", "B", "C", "D", "F"])

    num_A_stu = 0
    num_B_stu = 0
    tot_rec = 0
    print(" # Student\tGrade\n--------------------------")

    for i in range(size):
        tot_rec += 1
        grade = lst_stu_grades[i]
        st_name = lst_stu_names[i]
        if grade == 'A':
            message = '*'
        elif grade == 'B':
            message = '**'
        else:
            message = " "
        
        print(f"{tot_rec:>2d}. {st_name:<11}\t{grade}\t{message:>2}")
    for i in range(size):
        grade = lst_stu_grades[i]
        if grade == 'A':
            num_A_stu += 1
            
        elif grade == 'B':
            num_B_stu += 1

    print()
    print(f"Total Students   : {size:>2}")
    print(f"'A' Students     : {num_A_stu:>2} ({num_A_stu*100/tot_rec:>.1f}%)")
    print(f"'B' Students     : {num_B_stu:>2} ({num_B_stu*100/tot_rec:>.1f}%)")
    print(f"'A', 'B' Students: {num_A_stu + num_B_stu:>2} ({(num_A_stu+num_B_stu)*100/tot_rec:>.1f}%)")

if __name__ == "__main__":
    main()