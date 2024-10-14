import re

# \d is for digits
# [a-zA-Z] is for alphabet
# \s is for whitespace character


expression = '\d*\s[a-zA-Z]*\s[a-zA-Z]*,[a-zA-Z]*\s[a-zA-Z]*,\d*,[a-zA-Z]*\s[a-zA-Z]*'

address_regex = re.compile(expression, re.VERBOSE)
