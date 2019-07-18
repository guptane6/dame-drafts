# -*- coding: utf-8 -*-
"""
@author: Neha
"""
import dame_algorithms
import unittest

class TestAlgorithm3(unittest.TestCase):

    def test_paper_example(self):
        s = {(2, 3)}
        delta = {(1,), (1, 2), (1, 3), (1, 5), (2,), (3,), (5,)}
        omega = {(1, 2, 3)}
        self.assertEqual(algo3GenerateNewActiveSets(s,delta), omega)
    
    
if __name__ == '__main__':
    unittest.main()