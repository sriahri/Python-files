# from collections import Counter
#
# user_input = input("Enter the input: ")  # Read input
# # Process the input for removing the punctuation
# cleaned_input = user_input.replace(",", "")
# cleaned_input = cleaned_input.replace(".", "")
# cleaned_input = cleaned_input.replace("?", "")
# cleaned_input = cleaned_input.replace("!", "")
# # Split the words from the sentence
# words = cleaned_input.split()
# # Count the number of times each word appeared into a dictionary
# # Where key is word and value is count.
# words_along_with_count = Counter(words)
# # Sort the words based on count in ascending order
# sorted_words = sorted(words_along_with_count.items(), key=lambda x: (x[1], x[0]))
# # Print the output
# for res in sorted_words:
#     print('{}: {}'.format(res[0], res[1]))


x = 0
while x > 0:
    print(x, end='')
    x = x-1
print('Bye')
