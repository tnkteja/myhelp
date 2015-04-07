import unittest

from myhelp import myhelp

import types

from subprocess import Popen, PIPE, STDOUT

class TestAddFileOption(unittest.TestCase):

    def setUp(self):
        f=open("test.txt","w")
        f.write("This is a test string")
        f.close()


    def tearDown(self):
        os.remove("test.txt")


    def testModuleAvailablity(self):
        if isinstance(myhelp.run,types.FunctionType):
            self.assertTrue(True,"module available")
	else:
	    self.assertTrue(False)
        
    def testAddFileOption(self):
         myhelpP = Popen(['myhelp','-e', 'test.txt'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
         myhelpP.stdin.write("test testing tested\n")
         myhelpP.communicate()[0]
         myhelpP.stdin.close()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testModuleAvailablity']
    unittest.main()
