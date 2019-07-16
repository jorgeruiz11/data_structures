#!/usr/bin/env python
# -*- coding: utf-8 -*-

from interface import implements, Interface
from vertex_binary_tree import VertexBinaryTree

# Clase para arboles binarios.
class BinaryTree(object):

    # Clase vertice que implementa la interfaz vertice arbol binario.
    class Vertex(implements(VertexBinaryTree)):

        # Inicializamos los valores requeridos.
        def __init__(self):
            element = None
            father = None
            left = None
            right = None
            color = None

        # Constructor.
        def Vertex(self, element):
            self.element = element

        # Método que nos dice si existe el padre.
        def has_father(self):
            return self.father != None

        # Método que nos dice si hay vertice izquierdo.
        def has_left(self):
            return self.left != None

        # Método que nos dice si hay vertice derecho.
        def has_right(self):
            return self.right != None

        # Método que nos da el padre.
        def get_father(self):
            return self.father

        # Método que nos da el vertice izquierdo.
        def get_left(self):
            return self.left

        # Método que nos da el vertice derecho.
        def get_right(self):
            return self.right

        # Método que nos da el elemento del vertice.
        def get(self):
            return self.element

        # Método que nos da el color del vertice.
        def get_color(self):
            return self.color

        ''' Termina la clase Vertex '''

    root = None
    elements = 0

    # Constructor.
    def binary_tree(self):
        self.root = None
        self.elements = 0

    def depth(self, vertex, i):
        pass
