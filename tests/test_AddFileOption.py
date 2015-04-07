import unittest

import myhelp

import os

class TestAddFileOption(unittest.TestCase):

    def setUp(self):
        f=open("test.txt","w")
        f.write("This is a test string")
        f.close()


    def tearDown(self):
        pass


    def testModuleAvailablity(self):
        if myhelp.myhelp.run:
            self.assertTrue(True,"module available")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testModuleAvailablity']
    unittest.main()