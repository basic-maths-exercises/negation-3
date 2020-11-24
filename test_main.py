import unittest
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_negation_function(self) :
        source = inspect.getsource(negationOutside)
        self.assertTrue( source.find("if")!=-1, "Your function for the negation should contain an if" )
        self.assertTrue( numberOutside(data,1,9)==len(data) - negationOutside(data,1,9), "Your function for the negation is not returning the expected number" )
        self.assertTrue( numberOutside(data,2,7)==len(data) - negationOutside(data,2,7), "Your function for the negation is not returning the expected number" )
        self.assertTrue( numberOutside(data,4,6)==len(data) - negationOutside(data,4,6), "Your function for the negation is not returning the expected number" )
