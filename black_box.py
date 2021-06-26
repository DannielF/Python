import unittest

def sum(num_1, num_2):
    return num_1 + num_2

class BlackBox(unittest.TestCase):

    def test_sum_two_positive(self):
        num_1 = 10
        num_2 = 5

        result = sum(num_1, num_2)

        self.assertEqual(result, 15)

    def test_sum_two_negatives(self):
        num_1 = -10
        num_2 = -7

        result = sum(num_1, num_2)

        self.assertEqual(result, -17)    

if __name__ == '__main__':
    unittest.main()        