#first step in creating a linked list is to create a node class which will represent each node in the linked list
class Node:
    def __init__(self, data):#
        self.data = data     #[10]->[20]->[30]
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None #represents the first node of the linked list
        self.tail = None #represents the last node of the linked list
    #Add a node at the end of the linked list
    def add_node_end(self, value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node #Assign the address
            self.tail=new_node #Shift the tail pointer in last node

    def add_node_beg(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head #Assign the address of head to new node
            self.head=new_node #Shift the head pointer in first node

    def search_node(self, value):
        current = self.head
        position = 0
        while current:
            if current.data == value:
                print(f"Node found at position: {position}")
                return position
            current = current.next
            position += 1
        print("Node not found")
        return -1
        


    #display linked list
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")
linkedlistObj=LinkedList()
linkedlistObj.add_node_end(10)
linkedlistObj.add_node_end(20)
linkedlistObj.add_node_end(30)
linkedlistObj.add_node_end(40)
linkedlistObj.display()
linkedlistObj.add_node_beg(5)
linkedlistObj.add_node_beg(2)
linkedlistObj.add_node_beg(1)
linkedlistObj.display()
linkedlistObj.search_node(20)
linkedlistObj.search_node(100)