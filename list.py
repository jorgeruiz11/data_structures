#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
File: list.py
Autor: Jorge Ruiz.
'''

# Clase para listas doblemente ligadas en python.
class List(object):


    # Clase Nodo.
    class Node(object):

        # Atributos del nodo.
        element = None
        previous = None
        next = None


        # Constructor.
        def __init__(self, element):
            self.element = element


    # Atributos de la lista.
    head = None
    tail = None
    length = 0


    # Método que regresa la longitud de la lista.
    def get_length(self):
        return self.length


    # Si la lista era vacía el elemento a añadir será la cabeza y la cola, si no
    # creamos un nodo de apoyo que haga referencia a la cola actual (para no perderla)
    # después definimos al siguiente de la cola (actual) como el nuevo nodo y ahora
    # definimos la cola como el nuevo nodo, entonces la cola ya esta al final y ahora
    # el anterior al nuevo nodo será la cola anterior (la de antes de agregar el nuevo).
    def add_end(self, element):
        new_node = self.Node(element)

        if length == 0:
            self.head = self.tail = new_node
        else:
            support_node = self.tail
            self.tail.next = new_node
            self.tail = new_node
            new_node.previous = support_node

        self.length += 1


    # Si la lista era vacía el elemento a añadir será la cabeza y la cola, si no
    # creamos un nodo de apoyo que haga referencia a la cabeza actual (para no perderla)
    # después definimos al anterior de la cabeza (actual) como el nuevo nodo y ahora
    # definimos la cabeza como el nuevo nodo, entonces la cabeza buelve al inicio y ahora
    # el siguiente al nuevo nodo será la cabeza anterior (será el "apuntador" del nodo de apoyo).
    def add_start(self, element):
        new_node = self.Node(element)

        if length == 0:
            self.head = self.tail = new_node
        else:
            support_node = self.head
            self.head.previous = new_node
            self.head = new_node
            new_node.next = support_node

        self.length += 1


    # Si el la lista es vacía o el índice es igual a 0, agregamos al inicio, si la
    # longitud es igual al indice, es decir el inidice donde se quiere insertar el elemento
    # es mayor al último índice de la lista, entonces lo agregamos al final, en cualquier
    # otro caso, buscamos el elemento a reemplazar.
    def add(self, element, index):
        new_node = self.Node(element)

        if self.length == 0 or index == -1:
            self.add_start(new_node)
        elif self.length == index:
            self.add_end(new_node)
        else:
            support_node = self.head
            i = 0

            while (i < self.length):
                if support_node.get_index(element) == index:
                    new_node.previous = support_node.previous
                    new_node.next = support_node.next
                    support_node = new_node

                support_node = support_node.next
                i += 1


    # Método para buscar un elemento, si el elemento está en la cabeza entonces
    # regresamos la cabeza, si está en la cola regresamos la cola y si no recorremos
    # la lista hasta encontrarlo.
    def search_node(self, element):
        head_node = self.head
        tail_node = self.tail

        if head_node.element == element:
            return head_node
        elif tail_node.element == element:
            return tail_node
        else:
            while (head_node.next != None):
                if head_node.element == element:
                    return head_node
                else:
                    head_node = head_node.next

            return None


    # Si la lista no tiene elementos mandamos un error, de lo contrario quitamos el
    # primer elemento de la lista.
    def remove_first(self):
        try:
            support_node = self.head
            self.head = self.head.next
            self.length -= 1
            return support_node
        except NoSuchElementException as nsee:
            print("The list has no elements.")


    # Si la lista no tiene elementos mandamos un error, de lo contrario quitamos el
    # último elemento de la lista.
    def remove_last(self):
        try:
            support_node = self.tail
            self.tail = self.tail.previous
            self.length -= 1
            return support_node
        except NoSuchElementException as nsee:
            print("The list has no elements.")


    # Si el elemento a eliminar está en la cabeza entonces quitamos la cabeza, si el
    # elemento está en la cola entonces quitamos la cola, sino buscamos el elemento
    # y lo quitamos de la lista (haciendo que los "apuntadores" de su siguiente y su anterior
    # ya no lo "señalen").
    def remove(self, element):
        chosen = self.search_node(element)

        if self.head.element == element:
            remove_first()
        elif self.tail.node == element:
            remove_last()
        elif self.get_length > 0 and chosen != None:
            support_node = chosen
            support_node.next.previous = chosen.previous
            support_node.previous.next = chosen.next
            self.length -= 1


    #
    def contains(self, element):
        support_node = self.head


    # Método que recibe un elemento y lo busca en la lista, si el elemento se
    # encuentra en la lista, regresaremos su índice, sino se regresa -1.
    def get_index(self, element):
        support_node = self.head
        i = 0

        while (i < self.length):
            if support_node.element == element:
                return i

            support_node = support_node.next
            i += 1

        return -1
