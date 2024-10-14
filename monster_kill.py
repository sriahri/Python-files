n = int(input())
h = int(input())
a0, b0 = map(int, input().split())
monsters = []
for i in range(n):
    x, y = map(int, input().split())
    # Store the monsters
    monsters.append([x, y])
# Find the order in which the monsters are to be selected
order_to_be_killled = sorted(monsters, key=lambda x:b0/x[1])
for i in order_to_be_killled:
    combat = i[0]
    health = i[1]
    # check whether the hero can kill the monster or not
    if b0/combat >= health/a0:
        b0 = b0%combat + h
    else:
        print('NO')
        break
else:
    print('YES')