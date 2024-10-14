txt_file = open("randomaddresses.txt", 'r')
csv_file = open("output.csv", "w")
lines = txt_file.readlines()
for line in lines:
    street = line.rstrip("\n")
    tokens = line.split(",")
    city = tokens[0]
    tokens2 = tokens[1].split()
    state = tokens2[0]
    zipcode = tokens2[1]
    csv_file.write(street + "," + city + "," + state + "," + zipcode + "\n")
txt_file.close()
csv_file.close()
