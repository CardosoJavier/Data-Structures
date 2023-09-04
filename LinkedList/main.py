from LinkedList import LinkedList
from Node import Node

if __name__ == "__main__":
    myList: LinkedList = LinkedList()

    myArr: list = [1,2,3,4,5]
    myList.listToLinkedList(myArr)

    myList.printFromHead()

    val: int = 8
    searchVal: Node = myList.findValue(val)
    
    print("Not in list") if searchVal == None else print(f"searchVal with value {val} is at {searchVal}")
