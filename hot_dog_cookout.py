if __name__ == '__main__':
    people = int(input("Enter the number of people: "))
    hot_dogs_for_people = []
    for i in range(people):
        hot_dogs_for_people.append(int(input("Enter the hot dog for person {}: ".format(i + 1))))

    total_hot_dogs = sum(hot_dogs_for_people)
    hot_dogs_left_over = 10 - total_hot_dogs % 10 if total_hot_dogs % 10 != 0 else 0
    hot_dog_packages_required = total_hot_dogs // 10 if hot_dogs_left_over == 0 else total_hot_dogs // 10 + 1

    hot_dog_buns_left_over = (8 - total_hot_dogs * 2 % 8) if total_hot_dogs * 2 % 8 != 0 else 0
    hot_dog_bun_packages_required = total_hot_dogs * 2 // 8 if hot_dogs_left_over == 0 else total_hot_dogs * 2 // 8 + 1

    print("Hot dog packages required: {}".format(hot_dog_packages_required))
    print("Hot dogs left over: {}".format(hot_dogs_left_over))
    print("Hot dog bun Packages required: {}".format(hot_dog_bun_packages_required))
    print("Hot dog buns left over: {}".format(hot_dog_buns_left_over))
