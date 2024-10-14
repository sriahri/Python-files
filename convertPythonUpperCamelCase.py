def DifferentCases(str):
    result = str[0].upper()
    i = 1
    while i < len(str):
        if not str[i].isalnum():
            result += str[i + 1].upper()
            i += 1
        else:
            result += str[i].lower()
        i += 1
    return result


print(DifferentCases("cats AND*Dogs-are Awesome"))


def caesarCipher(str, num):
    result = ''
    for i in str:
        if i.isalpha():
            if i.isupper():
                result += chr((ord(i) + num) % 26 + 65)
            else:
                result += chr((ord(i) + num) % 26 + 97)
        else:
            result += i
    return result


def RunLength(strParam):
    encoding = ""
    i = 0
    while i < len(strParam):
        count = 1

        while i + 1 < len(strParam) and strParam[i] == strParam[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + strParam[i]
        i = i + 1
    return encoding


def FirstFactorial(num):
    if num == 0:
        return 1
    i = num
    fact = 1

    while num / i != num:
        fact = fact * i
        i -= 1
    return fact

def SumMultiplier(arr):
    arr.sort()
    total = sum(arr)

    final = total * 2
    if arr[0] * arr[1] > final or arr[-1] * arr[-2] > final:
        return True
    else:
        return False