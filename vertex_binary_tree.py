#!/usr/bin/env python
# -*- coding: utf-8 -*-

from interface import implements, Interface

# Interfaz para los vertices de un árbol binario.
class VertexBinaryTree(Interface):

    # Nos dice si hay padre.
    def has_father(self):
        pass

    # Nos dice si hay vertice izquierdo.
    def has_left(self):
        pass

    # Nos dice si hay vertice derecho.
    def has_right(self):
        pass

    # Nos da el vertice padre.
    def get_father(self):
        pass

    # Nos da el vertice izquierdo.
    def get_left(self):
        pass

    # Nos da el vertice derecho.
    def get_right(self):
        pass

    # Nos da el elemento del vertice.
    def get(self):
        pass

    # Nos da el color del vertice.
    def get_color(self):
        pass
