#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: test_list.py
Author: Jorge Ruiz.
"""

import unittest
from list import List

class TestList(unittest.TestCase):

    """
    * La falla en add puede estar en que add_end() no regresa nada entonces al hacer
      List.add_end(List, '3') dentro del assertEqual puede ser que por eso sea None != [3]
    * Para que no se vaya modificando la lista "global" creo que puedo crear una lista
      dentro de cada test para modificar solo esa.
    """

    # Prueba unitaria para el método de agrega final en la clase lista.
    def test_add_end(self):
        List.add_end(List, '4')
        self.assertEqual(List.to_string(List), '[4]')
        print(List.to_string(List))

    # Prueba unitaria para el método de agrega inicio en la clase lista.
    def test_add_start(self):
        List.add_start(List, '3')
        self.assertEqual(List.to_string(List), '[3, 4]')
        print(List.to_string(List))

    # Prueba unitaria para el método de elimina primero en la clase lista.
    def test_remove_first(self):
        l = List()
        l.remove_first()
        self.assertEqual(l.to_string(), '[4]')
        print(l.to_string() + "remove method")

    # Prueba para el método que regresa la longitud en la clase lista.
    def test_get_length(self):
        self.assertEqual(List.get_length(List), 2)
        print(List.to_string(List))



if __name__ == '__main__':
    unittest.main()
