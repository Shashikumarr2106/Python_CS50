import unittest
from bank import value

class TestValueFunction(unittest.TestCase):

    def test_starts_with_hello(self):
        result = value("Hello, world!")
        self.assertEqual(result, 0)

    def test_starts_with_h(self):
        result = value("Hi there")
        self.assertEqual(result, 20)

    def test_starts_with_h_case_insensitive(self):
        result = value("hello, how are you?")
        self.assertEqual(result, 0)

    def test_starts_with_h_other_case(self):
        result = value("Hurray! Let's go.")
        self.assertEqual(result, 20)

    def test_starts_with_other_letter(self):
        result = value("Greetings")
        self.assertEqual(result, 100)

    def test_empty_string(self):
        result = value("")
        self.assertEqual(result, 100)

if __name__ == '__main__':
    unittest.main()
