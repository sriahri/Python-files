from collections import Counter, defaultdict
from itertools import permutations

s1 = input()
s2 = input()
s1 = [str(i) for i in s1]

for i in range(len(s2)):
    if s2[i] in s1:
        s1.remove(s2[i])

difference_string = ''.join(s1)

print(difference_string)

d = Counter(difference_string)
print(d)
palindrome = True  # abccba -> a:2, b:2, c:2 | malayalam -> m:2, a:4
odd_character = ''
if len(difference_string) % 2 == 0:
    for letter_count in d.values():
        if letter_count % 2 != 0:
            palindrome = False
            break
else:
    count = 0
    for letter in d.keys():
        if d[letter] % 2 != 0 and count > 1:
            palindrome = False
            odd_character = ''
            break
        elif d[letter] % 2 != 0 and count == 0:
            count += 1
            odd_character = letter


print("Yes") if palindrome else print('No')

palindromes = set()
if palindrome:
    half_string = '' # e
    for letter in d.keys():
        half_string += letter * (d[letter]//2)

    palindrome_string = ''
    for p in permutations(half_string): # e p = ('e',)
        palindrome_string = ''.join(p) + odd_character + ''.join(p[::-1])
        if palindrome_string not in palindromes:
            print(palindrome_string)
            palindromes.add(palindrome_string)