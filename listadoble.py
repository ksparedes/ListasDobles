class Node:

    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None 

class doblelista:
    def __init__(self):
        self.head= None #Inicio de la lista
        self.tail= None #Final de la lista

    def insertar(self,data):
       
        if self.head is None:
            self.head= new_node
            self.tail=new_node

        else:
            new_node.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node


class Multilista:
    