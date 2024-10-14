if __name__ == '__main__':
    user_feet = int(input("Enter the feet obtained ny the user: "))
    area_obtained = user_feet * user_feet

    area_required_by_cow = 100
    number_of_cows = area_obtained // area_required_by_cow

    print("The number of cows are {}".format(number_of_cows))
