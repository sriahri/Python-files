if __name__ == '__main__':
    inFile = open("drones.txt", "r")
    outFile = open("drones_output.txt", 'w')
    lines = inFile.readlines()
    count = 0
    for i in lines[1:]:
        count += 1
    outFile.write("The number of strikes are {}\n".format(count))

    for line in lines[1:]:
        events = line.strip("\n").split(" ")

    for i in range(len(events)):
        events[i] = events[i].strip()
    final = []
    for i in events:
        x = i.replace(" ", "")
        if len(i) > 0:
            final.append(i)
    events = final.copy()
    strikes_count = 0
    for line in lines[1:]:
        # for i in events:
        #     print(i)
        events = line.strip("\n").split(" ")
        final = []
        for i in events:
            x = i.replace(" ", "")
            if len(i) > 0:
                final.append(i)
        events = final.copy()
        if events[4].lower().strip() == "morning":
            strikes_count += 1
    outFile.write("The number of strikes in the morning are {}\n".format(strikes_count))

    strikes_count = 0
    for line in lines[1:]:
        events = line.strip("\n").split(" ")
        final = []
        for i in events:
            x = i.replace(" ", "")
            if len(i) > 0:
                final.append(i)
        events = final.copy()
        if events[4].lower().strip() == "night":
            strikes_count += 1
    outFile.write("The number of strikes in the night are {}\n".format(strikes_count))

    civilians_killed = 0
    for line in lines[1:]:
        events = line.strip("\n").split(" ")
        final = []
        for i in events:
            x = i.replace(" ", "")
            if len(i) > 0:
                final.append(i)
        events = final.copy()
        civilians_killed += int(events[7].strip())
    outFile.write("The minimum number of civilians killed are {}\n".format(civilians_killed))

    children_killed = 0
    for line in lines[1:]:
        events = line.strip("\n").split(" ")
        final = []
        for i in events:
            x = i.replace(" ", "")
            if len(i) > 0:
                final.append(i)
        events = final.copy()
        children_killed += int(events[9].strip())
    outFile.write("The minimum number of children killed are {}\n".format(children_killed))

    strikes_after_2012 = 0
    for line in lines[1:]:
        events = line.strip("\n").split(" ")
        for i in events:
            x = i.replace(" ", "")
            if len(i) > 0:
                final.append(i)
        events = final.copy()
        date = events[1].split('/')[2]
        if int(date) >= 2012:
            strikes_after_2012 += 1
    outFile.write("The number of strikes after 2012 are {}\n".format(strikes_after_2012))

    location_strikes = {}
    for line in lines[1:]:
        events = line.strip("\n").split(" ")
        for i in events:
            x = i.replace(" ", "")
            if len(i) > 0:
                final.append(i)
        events = final.copy()
        location = events[3].lower()
        miminum_civilians = int(events[7].strip())
        if location in location_strikes:
            location_strikes[location] += miminum_civilians
        else:
            location_strikes[location] = miminum_civilians

    highest = 0
    highest_location = ""
    for i in location_strikes.keys():
        if location_strikes[i] > highest:
            highest_location = i
    outFile.write("The highest value of minimum civilians reported killed is {}\n".format(highest_location))
