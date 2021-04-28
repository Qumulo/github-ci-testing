import unittest

class HelloWorldTest(unittest.TestCase):

    def test_math(self):
        self.assertEqual(2 + 2, 4)

    def test_string(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()
