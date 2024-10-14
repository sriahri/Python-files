def listSum(LL):
    Done = False
    sum =0
    (node, link) = LL
    while not Done:
        sum += node
        (node, link) = link

        if link == None:
            Done = True
        else:
            (node, link) = link

    return sum

def display(LL):
    Done = False
    (node, link) = LL
    while not Done:
        (node, link) = link
        print(node)

        if link == None:
            Done = True
        else:
            (node, link) = link


def disp(LL):
    node = LL
    while node[1] != None:
        print(node[0])
        node = node[1]

x = None
for i in range(0, 6, 2):
    x = [i, x]

print(x)
print()
print()
disp(x)


# muList = (1, (2, (3, (4, None))))
# display(muList)
# sum = listSum(muList)
# print(sum)
