#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: test_list.py
Author: Jorge Ruiz.
"""

import unittest
from list import List

class TestList(unittest.TestCase):

    # Prueba unitaria para el método de agrega final en la clase lista.
    """
    La falla puede estar en que add_end() no regresa nada entonces al hacer
    List.add_end(List, '3') dentro del assertEqual puede ser que por eso sea None != [3]
    """
    def test_add_end(self):
        List.add_end(List, '3')
        self.assertEqual(List.to_string(List), '[3]')
        print(List.to_string(List))

    # Prueba para el método que regresa la longitud en la clase lista.
    def test_get_length(self):
        self.assertEqual(List.get_length(List), 1)



if __name__ == '__main__':
    unittest.main()
