def choices_choices(candidate, pattern, possibility):
    if len(candidate) == 1:
        possibility.append(pattern.replace('_', candidate[0]))
        return
    possibility.append(pattern.replace('_', candidate[0]))
    return choices_choices(candidate[1:], pattern, possibility)


if __name__ == '__main__':
    p = []
    choices_choices(['t', 'p', 'h'], '_ower', p)
    print(p)
