import re


def starts_with_non_number(s):
    if s[0].isdigit():
        return False
    return True


def multiple_words(s):
    s = s.strip()
    words = s.split()
    if len(words) > 1:
        return True
    return False


def reserved_us_tld(s):
    if s.startswith('https') and (s.endswith('.gov') or s.endswith('.edu') or s.endswith('.mil')):
        return True
    return False
