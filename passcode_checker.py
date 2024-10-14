def passcode_checker(attempts):
    num = 0
    for i in range(len(attempts)):
        if attempts[i].lower() == 'failed':
            num += 1

    if num < 3:
        return "Good memory!"

    elif num == 3 or num == 4:
        return "Enter passcode with caution!"

    elif num >= 5:
        return "You should really remember your passcode!"


# Sample attempt list
attempts = ['failed', 'failed', 'failed', 'failed', 'failed', 'failed', 'succeeded']
i = 'failed'
num = attempts.count('failed')
print(passcode_checker(attempts))
