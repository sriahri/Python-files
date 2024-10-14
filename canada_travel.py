def isFullyVaccinated (vaccines_list):
    flag = False
    if len(vaccines_list) == 2:
        if vaccines_list[0] == 'F' or 'M' and vaccines_list[1] == 'M' or 'F':
            flag = True
        elif vaccines_list[0] == 'A' and vaccines_list[1] == 'M' or 'F':
            flag = True
        elif vaccines_list[1] == 'A' and vaccines_list[0] == 'M' or 'F':
            flag = True
    return flag

def isAllowed(vaccines_list, test, lastVisited ):
    banned = ["South Africa", "Mexico", "Australia", "Germany"]
    result = False
    flag = isFullyVaccinated(vaccines_list)
    if flag:
        if test:
            for i in lastVisited:
                if i in banned:
                    break
            else:
                result = True
    return result

vaccines = ['F', 'M']
test_negative = True
last_visited = ['China', 'USA']
print(isAllowed(vaccines, test_negative, last_visited))
vaccines = ['F', 'M']
test_negative = True
last_visited = ['China', 'Germany']
print(isAllowed(vaccines, test_negative, last_visited))