import unittest
from five_multiply import five_multiply

class TestMultiplyFive(unittest.TestCase):

    def test_five_multiply(self):
        self.assertEqual(five_multiply(5), 25, 'Should return 25')
        
if __name__ == '__main__':
    unittest.main()
