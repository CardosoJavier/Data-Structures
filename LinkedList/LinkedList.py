from Node import Node


class LinkedList:

    # constructor
    def __init__(self):

        # linked list head
        self.head: Node = None


    """
        Prints list starting from the list's head

        @params: None
        @return: None
    """
    def printFromHead(self) -> None:

        if (self.head == None):
            print("Empty linkedList")
            return

        current: Node = self.head

        while (current != None):
            print(f"{current.data} -> ", end="")
            current = current.nextNode
        print('None')


    """
        Adds item at the beginning of the list

        @params:
            data (any): data/element to be inserted in the list
        @return: None
    """
    def addFirst(self, data: any) -> None:

        # List is empty
        if self.head == None:
            self.head = Node(data)

        # create new node and make it the new head
        else:
            newNode: Node = Node(data)
            newNode.nextNode = self.head
            self.head = newNode


    """
        Adds item at the end of the list

        @params:
            data (any): data to be inserted in the list
        @return: None
    """
    def addLast(self, data) -> None:

        # List is empty
        if (self.head == None):
            self.head = Node(data)
        
        # Create new node and insert it at the end of the list
        else:
            newNode: Node = Node(data)

            current: Node = self.head
            while (current.nextNode != None):
                current = current.nextNode

            current.nextNode = newNode

    
    """
        Delete entire list

        @params: None
        @return: None
    """
    def deleteList(self) -> None:
        currentNode: Node = self.head
        saveNext: Node = None

        while (currentNode != None):
            saveNext = currentNode.nextNode
            del currentNode
            currentNode = saveNext
        
        self.head = None


    """
        Delete specific value

        @params:
            value (any): value to be deleted
        @return: None
    """
    def deleteValue(self, value):
        if (self.head == None):
            return
        
        if (self.head.data == value):
            self.head = self.head.nextNode

        savePrev: Node = None
        current: Node = self.head

        while (current != None):
            if (current.data == value):
                savePrev.nextNode = current.nextNode
                del current
                return

            savePrev = current
            current = current.nextNode

    
    """
        Find a value in the list and return its node

        @params:
            value (any): Value to be find in the linked list
        @return:
            (Node) Node with the value
    """
    def findValue(self, value) -> Node:

        current: Node = self.head

        while (current != None) :
            if (current.data == value):
                return current
            current = current.nextNode

        return None


    """
        Create linked list from array

        @params:
            arr (array):  Array that will be converted into a linked list
        @return: Node
    """
    def listToLinkedList(self, arr: list):
        
        # return if list is empty
        if (len(arr) <= 0):
            print("List is empty")
        
        else: 
            self.head = Node(arr[0])
            current: Node = self.head

            for i in range(1, len(arr)):
                newNode: Node = Node(arr[i])
                current.nextNode = newNode

                current = current.nextNode