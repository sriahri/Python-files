from typing import Sequence


file = open("output.fas", "r")
lines = file.readlines()
sequences = []
for i in lines:
    sequences.append(i.split()[1])
for i in range(len(sequences)):
    for j in range(i+1, len(sequences)):
        count = 0
        length = min(len(sequences[i]), len(sequences[j]))
        for k in range(length):
            if sequences[i][k] == sequences[j][k]:
                count += 1
        print("Match of sequence{} and sequence{} is {}%".format(i+1, j+1, count/length * 100))