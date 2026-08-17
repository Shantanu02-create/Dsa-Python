import sys
class Queue:
    def __init__(self,queuesize):
        self.QueueSize=queuesize
        self.myQueue=[]
    def isFull(self):
        if len(self.myQueue)==self.QueueSize:
            return True
        else:
            return False
    def isEmpty(self):
        if len(self.myQueue)==0:
            return True
        else:
            return False
    def Enqueue(self,value):
        if self.isFull():
            print("Queue is Full")
        else:
            self.myQueue.append(value)
            print("Item Enqueued in Queue:",value)
    def Dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            value=self.myQueue.pop(0)
            print("Item Dequeued from Queue:",value)


    def PeekFront(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            value=self.myQueue[0]
            print("Front item in Queue:",value)

    def PeekRear(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            value=self.myQueue[-1]
            print("Rear item in Queue:",value)

    def deleteQueue(self):
        self.myQueue=None
        print("Queue Deleted")
    def displayQueue(self):
        print(self.myQueue)
size=int(input("Enter size of Queue:"))
obj=Queue(size)
while True:
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.isEmpty")
    print("4.Peek Front Value ")
    print("5.Delete Queue")
    print("6.Display Queue")
    print("7.is Full")
    print("8.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        value=int(input("Enter the value:"))
        obj.Enqueue(value)
    if choice==2:
        obj.Dequeue()
    if choice==3:
        print(obj.isEmpty())
    if choice==4:
        obj.PeekFront()
    if choice==5:
        obj.deleteQueue()
    if choice==6:
        obj.displayQueue()
    if choice==7:
        print(obj.isFull())
    if choice==8:
        sys.exit()

    
    

    
                