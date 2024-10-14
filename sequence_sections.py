for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    energy_cost = 0
    old_string = ''
    new_string = s[0:k]
    for i in range(len(s) - k + 1):
        old_string = new_string
        new_string = s[i:i+k]
        difference = sum(1 for a, b in zip(new_string, old_string) if a != b)
        energy_cost += difference
    print(energy_cost)
