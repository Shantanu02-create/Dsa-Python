#Pop removes top item from stack and returns it and peek returns the top item without removing it. Both methods raise an exception if the stack is empty.
#two types of implementing Stack: Array/List(Easy Implementation) & LinkedList(Fast Performance)

#Stack Implementation using List/Array
import sys
class Stack:
    #Constructor
    def __init__(self,stackSize):
        self.stackSize=stackSize
        self.myStack=[]#list represent the stack in python
    #isFull Condition check
    
    def isFull(self):
        if len(self.myStack)==self.stackSize:
            return True
        else:
            return False
        
#isEmpty Condition
    def isEmpty(self):
        if len(self.myStack)==0:
            return True
        else:
            return False

    def Push(self,value):
        if self.isFull():
            print("Stack is Full")
        else:
            self.myStack.append(value)
            print("Item pushed in stack:",value)
    def Pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            value=self.myStack.pop()
            print("Item popped from stack:",value)
    def Peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            value=self.myStack[-1]
            print("Top item in stack:",value)

    def deleteStack(self):
        self.myStack=None
        print("Stack Deleted")

    def displayStack(self):
        print(self.myStack)

size=int(input("Enter Size of stack:"))
obj=Stack(size)#Object has created for stack Class
while True:
    print("1.Push operation")
    print("2.Pop operation")
    print("3.Peek operation")
    print("4.isFull")
    print("5.isEmpty")
    print("6.Delete Stack")
    print("7.Display Stack")
    print("8.Exit")
    choice=int(input("Enter choice:"))
    if choice==1:
        value=int(input("Enter value to push in Stack:"))
        obj.Push(value)
    elif choice==2:
        obj.Pop()
    elif choice==3:
        obj.Peek()
    elif choice==4:
        print(obj.isFull())
    elif choice==5:
        print(obj.isEmpty())
    elif choice==6:
        obj.deleteStack()
    elif choice==7:
        obj.displayStack()
    else:
        sys.exit()
