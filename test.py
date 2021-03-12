__author__ = 'JYOTHSNA'
import unittest
import Simple_Calculator

#A series of tests designed to see if the functions fail
class ArithTest (unittest.TestCase):

    def runTest (self):


        self.failUnless(Simple_Calculator.add(1, 2) == 3, msg='1+2 = 3 failed')

        self.failIf(Simple_Calculator.divide(10, 2) == 3, msg='10/2 = 3 fail test failed')

        self.failUnlessEqual(Simple_Calculator.multiply(2, 2), 4, msg='2 * 2 failed')

        self.assertTrue(Simple_Calculator.subtract(13, 6) == 7, msg='13 - 6 failed')

        self.assertTrue(Simple_Calculator.multiply(5, 5) == 25, msg='5 * 5 failed')

        self.assertEqual(Simple_Calculator.add(10, 15), 25, msg='10 + 15 = 25 failed')




def suite():

    suite = unittest.TestSuite()

    suite.addTest (ArithTest())

    return suite





if __name__ == '__main__':

    runner = unittest.TextTestRunner()

    test_suite = suite()

    runner.run (test_suite)