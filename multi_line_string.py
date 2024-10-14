input_string = '''Dell Display Manager’s (DDM) Easy Arrange feature lets you quickly tile and view your applications side by side across one or more connected screens for multitasking efficiency. 
And with the improved DDM, you’ll get even more preset layouts.
The auto-restore feature remembers where you left off, so applications will go back to where you left them, even after you’ve unplugged.'''

print(input_string) # Printing the input string.
print() # To distinguish the output.
sentences_list = tuple(input_string.split('\n')) # Based on the new line character, we divide the string into group of sentences.
# The above one contains the sentences as the line 1 in index 0, line 2 in index 1 and so on....
# Using format() we change the position of the sentences and store it in the variable.
print()
inputStringNew = "{2}{0}{1}".format(*sentences_list)
print(inputStringNew) # Print the new input string.
print()
# Now we split the input string based on '.' and the list contains the sentences
# without any '.' at the end. By using indexing and slicing, we print the sentence.
outputString = inputStringNew.split('.')[2][28:]
print(outputString)
print()
count = 0
# Counting the number of characters in the input string.
for i in input_string:
    if i != 'D':
        count += 1
    
print('The number of characters is',count)