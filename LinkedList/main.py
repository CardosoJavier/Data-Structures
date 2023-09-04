from LinkedList import LinkedList
from Node import Node

if __name__ == "__main__":
    myList: LinkedList = LinkedList()
    myList.addLast(1)
    myList.addLast(2)
    myList.addLast(3)
    myList.addLast(4)
    myList.addLast(5)

    myList.printFromHead()
    myList.deleteValue(1)
    myList.printFromHead()