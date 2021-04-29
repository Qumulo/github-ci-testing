import unittest

from main import add


class HelloWorldTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 2), 4)

    def test_string(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_always_fails(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
