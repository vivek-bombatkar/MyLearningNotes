import unittest

def my_fun(i:int = None):
    try:
        return i+1
    except TypeError:
        return None

class myTest(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(my_fun(3),4)
    def test_None(self):
        self.assertEqual(my_fun(),None)
    def test_str(self):
        self.assertEqual(my_fun('10'),None)
if __name__=='__main__':
    unittest.main()