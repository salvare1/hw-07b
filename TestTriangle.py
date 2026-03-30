# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isoceles')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene')

    def testNotATriangleEqualTwo(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle')

    def testNotATriangleTooLong(self):
        self.assertEqual(classifyTriangle(2, 3, 10), 'NotATriangle')

    def testInvalidZeroSide(self):
        self.assertEqual(classifyTriangle(0, 2, 2), 'InvalidInput')

    def testInvalidNegativeSide(self):
        self.assertEqual(classifyTriangle(-1, 2, 2), 'InvalidInput')

    def testInvalidTooLargeSide(self):
        self.assertEqual(classifyTriangle(201, 2, 2), 'InvalidInput')

    def testInvalidNonInteger(self):
        self.assertEqual(classifyTriangle(2.5, 2, 2), 'InvalidInput')

    def testBugDetectionZeroInSecondPosition(self):
        self.assertEqual(classifyTriangle(2, 0, 2), 'InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

