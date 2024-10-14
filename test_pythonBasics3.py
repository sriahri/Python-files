import unittest
import pythonBasics3


class TestPythonBasicsone(unittest.TestCase):
    # Test case for starts_with_non_number
    def test_starts_with_non_number(self):
        self.assertEqual(pythonBasics3.starts_with_non_number("Once upon a time, I was 18"), True)
        self.assertEqual(pythonBasics3.starts_with_non_number("5 weekdays each week"), False)
        self.assertEqual(pythonBasics3.starts_with_non_number("-5 is what I got on my quiz"), True)
        self.assertEqual(pythonBasics3.starts_with_non_number(" 1 more meal left in the fridge"), True)
        self.assertEqual(pythonBasics3.starts_with_non_number("# is used to comment a line in Python"), True)
        self.assertEqual(pythonBasics3.starts_with_non_number(',hello world'), True)
        self.assertEqual(pythonBasics3.starts_with_non_number(';what is this'), True)
        self.assertEqual(pythonBasics3.starts_with_non_number('109887645'), False)
        # Please add three more test cases following the order above

    # Test case for multiple_words
    def test_multiple_words(self):
        self.assertEqual(pythonBasics3.multiple_words("That's 10/10"), True)
        self.assertEqual(pythonBasics3.multiple_words(" "), False)
        self.assertEqual(pythonBasics3.multiple_words("Different\\twhitespace"), False)
        self.assertEqual(pythonBasics3.multiple_words("It's-all-one-word"), False)
        self.assertEqual(pythonBasics3.multiple_words(" one-sided?"), False)
        self.assertEqual(pythonBasics3.multiple_words('Hello World'), True)
        self.assertEqual(pythonBasics3.multiple_words('What,shall,we,do'), False)
        self.assertEqual(pythonBasics3.multiple_words('I;am;john'), False)

        # Please add three more test cases following the order above

    def test_reserved_us_tld(self):
        self.assertEqual(pythonBasics3.reserved_us_tld('https://www.abcd.gov'), True)
        self.assertEqual(pythonBasics3.reserved_us_tld('https://www.abcd.edu'), True)
        self.assertEqual(pythonBasics3.reserved_us_tld('https://www.abcd.mil'), True)
        self.assertEqual(pythonBasics3.reserved_us_tld('http://www.abcd.gov'), False)
        self.assertEqual(pythonBasics3.reserved_us_tld('https://www.abcd.com'), False)
        self.assertEqual(pythonBasics3.reserved_us_tld('https://www.abcd.mx'), False)
        self.assertEqual(pythonBasics3.reserved_us_tld('http://www.abcd.edu'), False)
        self.assertEqual(pythonBasics3.reserved_us_tld('http://www.abcd.mil'), False)
