#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: list.py
Author: Jorge Ruiz.
"""

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

        if self.length == 0:
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

        if self.length == 0:
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
            self.add_start(new_node.element)
        elif self.length == index:
            self.add_end(new_node.element)
        else:
            support_node = self.head
            i = 0

            # Checar caso donde el indice es 1 mejor a la longitud.
            while (i < self.length):

                if self.get_index(support_node.element) == index:
                    new_node.previous = support_node.previous
                    new_node.next = support_node.next
                    support_node.previous.next = new_node
                    support_node.next.previous = new_node
                    support_node = new_node

                support_node = support_node.next
                i += 1

            self.length += 1


    # Método para buscar un elemento, si el elemento está en la cabeza entonces
    # regresamos la cabeza, si está en la cola regresamos la cola y si no recorremos
    # la lista hasta encontrarlo.
    def get_node(self, element):
        head_node = self.head
        tail_node = self.tail

        if head_node.element == element:
            return head_node
        elif tail_node.element == element:
            return tail_node
        else:
            while (head_node.next != None):
                if head_node.element == element:
                    return head_node #.element
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
        chosen = self.get_node(element)

        if self.head.element == element:
            self.remove_first()
        elif self.tail.element == element:
            self.remove_last()
        elif self.get_length() > 0 and chosen != None:
            support_node = chosen
            chosen.previous.next = support_node.next
            chosen.next.previous = support_node.previous
            self.length -= 1


    # Método booleano que nos dice si un elemento está en la lista o no.
    def contains(self, element):
        support_node = self.get_node(element)

        if self.length == 0:
            return False
        else:
            if support_node != None:
                return True
            else:
                return False


    # Método para obtener la reversa de la lista, simplemente creamos una vacía y
    # mientras recorremos (en la pasada), vamos agregando al inicio en la nueva.
    def reverse(self):
        new_list = self.List()
        support_node = self.head

        while support_node != None:
            new_list.add_start(support_node.element)
            support_node = support_node.next

        return new_list


    # Método para obtener la copia de la lista, simplemente creamos una vacía y
    # mientras recorremos (en la pasada), vamos agregando al final en la nueva.
    def get_copy(self):
        new_list = self.List()
        support_node = self.head

        while support_node != None:
            new_list.add_end(support_node)
            support_node = support_node.next

        return new_list


    # Volvemos todo None y la longitud de la lista como 0
    def clean(self):
        self.head.previous = None
        self.tail.next = None
        self.head = self.tail = None
        self.length = 0


    # Sólo devolvemos el primer elemento de lalista.
    def get_first(self):
        if self.head != None and self.length != 0:
            return self.head


    # Sólo devolvemos el último elemento de lalista.
    def get_last(self):
        if self.tail != None and self.length != 0:
            return self.tail


    # Método que recorre la lista buscando el elemento con  el indice dado y si lo
    # encuentra lo regresa.
    def get(self, i):
        support_node = self.head
        j = 0

        if i >= 0 and i < self.length:
            while j < i:
                support_node = support_node.next
                j += 1

            return support_node.element


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


    # Primero descartamos las opciones donde no podrían ser iguales, que son:
    # Si las longitudes son distintas, si el objeto recibido es nulo o si un elemento
    # es nulo y en la otra no. Si no pasó todo esto entonces serán iguales.
    def equals(self, recived_object):
        if self.length != recived_object.length or recived_object == None: # Falta hacer parse
            return False
        else:
            own = self.head
            unknown = recived_object.head

            while unknown != None:
                if unknown.element != own.element or (unknown == None and own != None):
                    return False

                unknown = unknown.next
                own = own.next

            return True


    #
    def to_string(self):
        if self.length == 0:
            return "[]"
        else:
            str = "["
            current_node = self.head
            t_node = self.tail

            while current_node != t_node:
                str += current_node.element + ", "
                current_node = current_node.next

            str += t_node.element + "]"

            return str





if __name__ == '__main__':
    l = List()
    l.add_end("1")
    l.add_end("2")
    l.add_end("3")
    l.add_end("4")
    l.remove("3")
    print(l.get_length())
    #l.add("4", 1)
    print(l.get_node("4"))
    #print(l.equals([1,2,3]))
    print(l.to_string())
    l.clean()
    print(l.to_string())
