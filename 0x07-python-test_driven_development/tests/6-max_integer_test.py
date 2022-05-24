#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):


    def test_positivenumbers(self):
        test_list = [1, 3, 8]
        self.assertEqual(max_integer(test_list), 8)
    
    def test_negativenumbers(self):
        test_list = [-1, -3, -8]
        self.assertEqual(max_integer(test_list), -1)

    def test_negativenumbers_nan(self):
        test_list = [-1, -3, -8, float('nan')]
        self.assertEqual(max_integer(test_list), -1)

    def test_numbers_specialdt(self):
        test_list = [-1, -3, -8, float('nan'), float('inf')]
        self.assertEqual(max_integer(test_list), float('inf'))

    def test_floatnumbers(self):
        test_list = [1, 1.75, 1.5]
        self.assertEqual(max_integer(test_list), 1.75)

    def test_onelement(self):
        test_list = ['one element']
        self.assertEqual(max_integer(test_list), 'one element')

    def test_string(self):
        """Test for string arguments """
        test_list = ['string1', 'string0', 'string2', 'Hi']
        self.assertEqual(max_integer(test_list), 'string2')
        
    def test_strings(self):
        """Test for string arguments """
        test_list = ['1', '2', '3', '4']
        self.assertEqual(max_integer(test_list), '4')

    def test_isempty(self):
        """Test for empty list"""
        test_list = ["", [], [None]]
        for i in test_list:
            self.assertEqual(max_integer(i), None)

    def test_inf_datatype(self):
        """Test for infinity number type"""
        test_list = [[1, 3, 8, float('inf')], [float('inf'), float('inf'), float('inf'), float('inf')]]
        for i in test_list:
            self.assertEqual(max_integer(i), float('inf'))


if __name__  == "__main__":
    unittest.main()
