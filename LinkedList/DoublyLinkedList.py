class node:
    def __init__(self,data):
        self.data= data
        self.next = None
        self.prev = None

class Doublylinklist:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,val):
        newnode= node(val)
        if self.length ==0:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.prev = self.tail
            self.tail.next = newnode
            self.tail = newnode
        self.length+=1
        return
    def Addatstart(self,val):
        newnode= node(val)
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode
        self.length+=1
        return
    def Insert(self,val,location):
        # newnode = node(val)
        if location==0:
            self.Addatstart(val)
        elif location==self.length:
            self.append(val)
        elif location > self.length:
            print("Invalid location")
        else:
            head = self.head
            while location>1:
                head=head.next
                location-=1
            newnode = node(val)
            head.next.prev = newnode
            newnode.next = head.next
            newnode.prev = head
            head.next = newnode
        self.length+=1
        return 
    def pop(self):
        if self.length==0:
            print("No Node exist")
            return
        self.tail = self.tail.prev
        self.tail.next= None
        self.length-=1
        return
    def DeleteAtStart(self):
        if self.length==0:
            print("No Node exist")
            return
        self.head = self.head.next
        self.length-=1
        return 

    def Removebyvalue(self,val):
        if self.length==0:
            print("No Node exist")
            return
        elif self.head.data ==val:
            self.DeleteAtStart()
            return
        else:
            head = self.head
            while head!=None:
                if head.data == val:
                    if head == self.tail:
                        self.pop()
                        return 
                    head.prev.next = head.next
                    head.next.prev = head.prev
                    self.length-=1
                    return
                head=head.next
        print("No such node found")
        return 
    def print(self):
        head = self.head
        while head!=None:
            print(head.data,end="==>")
            head=head.next
        print(None)
        return 
dll = Doublylinklist()
dll.append(0)
dll.append(1)
dll.append(2)
dll.append(4)
dll.append(5)
dll.append(6)
dll.append(7)
dll.append(8)
dll.Insert(9,8)
dll.print()

dll.Removebyvalue(9)
dll.print()
print(dll.length)