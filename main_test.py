import unittest

from main import add


class HelloWorldTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 2), 4)

    def test_string(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_bool(self):
        self.assertTrue(True)

    def test_bool_false(self):
        self.assertFalse(False)


if __name__ == '__main__':
    unittest.main()
