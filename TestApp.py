import unittest
from App import GetChart

class KnowValues(unittest.TestCase):

    # Checking get number function
    def test_get_num_item(self):
        result = GetChart().get_num_item("1")
        excepted = True
        self.assertEqual(excepted,result)
    


if __name__ == '__main__':
    unittest.main()
