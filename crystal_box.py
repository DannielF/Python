import unittest

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

class TestOfCrystal(unittest.TestCase):

    def test_is_adult(self):
        age = 20
        result = is_adult(age)
        self.assertEqual (result, True)

    def test_is_younger(self):
        age = 15
        result = is_adult(age)
        self.assertEqual (result, False)        

if __name__ == "__main__":
    unittest.main()

