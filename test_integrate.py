__author__ = 'JYOTHSNA'
import unittest
import Simple_Calculator

#A series of tests designed to see if the functions fail
class ArithTest_integration (unittest.TestCase):

    def runTest (self):


        self.assertEqual(Simple_Calculator.add(Simple_Calculator.multiply(1,1), Simple_Calculator.subtract(3,1)) , 3)

        self.assertEqual(Simple_Calculator.divide(Simple_Calculator.multiply(2,5), Simple_Calculator.add(1,1)) , 5)

        self.assertEqual(Simple_Calculator.multiply(Simple_Calculator.subtract(4,2), Simple_Calculator.divide(4,2)), 4)

        self.assertEqual(Simple_Calculator.subtract(Simple_Calculator.add(6,7), Simple_Calculator.divide(Simple_Calculator.multiply(6,2),2)) , 7)



def suite():

    suite = unittest.TestSuite()

    suite.addTest (ArithTest_integration())

    return suite





if __name__ == '__main__':
    runner = unittest.TextTestRunner()

    test_suite = suite()

    runner.run (test_suite)