import unittest
from class_definitions import NumberGuesser as ng


class TestNumberGuesser(unittest.TestCase):
    def setUp(self):
        a_list = [3, 4, 5, 6, 11, -2]
        self.ng = ng.NumberGuesser(a_list)

    def tearDown(self):
        del self.ng

    def test_constructor__init__(self):
        a_list = [3, 4, 5, 6, 11, -2]
        self.ng(a_list)

    def test_add_guess(self):
        a_list = [3, 4, 5, 6, 11, -2]
        self.ng.add_guess(a_list)


if __name__ == '__main__':
    unittest.main()
