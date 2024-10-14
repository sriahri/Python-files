def input_data():
    pairs = []
    for i in range(3):
        try:
            name, number = input().split()
            pairs.append(name)
            pairs.append(int(number))
        except Exception:
            pairs.append("None")
            pairs.append(0)
    result = ''
    for i in pairs:
        result += str(i)
        result += "\n"
    return result
