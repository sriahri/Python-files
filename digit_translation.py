def find_shortest_string_and_count(s):
    # Dictionary of digit words mapped to their corresponding numeric values
    digit_words = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    # Length of the input string
    n = len(s)

    # dp[i] = (minimum length of string starting at index i, number of distinct ways to achieve that length)
    dp = [(float('inf'), 0)] * (n + 1)

    # Base case: an empty string has length 0 and 1 way to achieve it
    dp[n] = (0, 1)

    # Process the string from right to left
    for i in range(n - 1, -1, -1):
        # Initially assume no replacement (carry forward the existing substring)
        dp[i] = (dp[i + 1][0] + 1, dp[i + 1][1])

        # Try all digit words only if they fit within the remaining string length
        for word, digit in digit_words.items():
            if i + len(word) <= n and s[i:i + len(word)] == word:
                # If we can replace the current word with a digit
                next_pos = i + len(word)
                new_len = dp[next_pos][0] + 1  # +1 for the digit replacement

                # If we found a shorter length, update
                if new_len < dp[i][0]:
                    dp[i] = (new_len, dp[next_pos][1])
                # If we found an equivalent length, add to the count
                elif new_len == dp[i][0]:
                    dp[i] = (dp[i][0], dp[i][1] + dp[next_pos][1])

    # The result for the entire string is stored in dp[0]
    shortest_length = dp[0][0]
    distinct_count = dp[0][1]

    return shortest_length, distinct_count


# Example Usage
s = input()
shortest_length, distinct_count = find_shortest_string_and_count(s)
print(shortest_length)
print(distinct_count)
