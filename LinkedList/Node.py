class Node:

    # constructor
    def __init__(self, data: any) -> None:
        self.data: any = data
        self.nextNode: Node = None