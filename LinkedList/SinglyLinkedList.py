class node:
    def __init__(self,data):
        self.data= data
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail=None
        self.length=0
    def isempty(self):
        return self.head==None
    def append(self,data):
        newnode= node(data)
        if self.isempty():
            self.head=newnode
            self.tail= self.head
        else:
            self.tail.next = newnode
            self.tail = newnode
            ##WE can also do this
            # head = self.head
            # while head.next!=None:
            #     head=head.next
            # head.next = newnode
        self.length+=1
        return self.head
    def GetNode(self,location):
        head = self.head
        if 0>location or location> self.len():
            print("Index doesn't exist.")
            return False
        while location >0:
            head=head.next
            location-=1
        return head
    def Insert(self,data,location):
        newnode= node(data)
        head = self.head
        if self.len()+1<location:
            print("Location doesn't exist")
            return
        if location==0:
            newnode.next=head
            self.head = newnode
        elif location == self.len()+1:
            self.append(data)
            return
        while location >2:
            head=head.next
            location-=1
        newnode.next = head.next
        # print(head.data,head.next.data)
        head.next = newnode
        return
        
    def len(self):
        return self.length
    def print(self):
        head = self.head
        while head!=None:
            print(head.data,end="==>")
            head=head.next
            # input()+
        print(None)
    def InLinkedlist(self,data):
        head = self.head
        while head!=None:
            if head.data==data:
                return True
            head=head.next
        return False
    def pop(self,data):
        if self.InLinkedlist(data):
            if self.head.data==data:
                self.head=self.head.next
                return 
            else:
                head = self.head
                prev= None
                while head!=None:
                    if head.data==data:
                        if head==self.tail:
                            self.tail = prev
                        prev.next = head.next
                        return 
                    else:
                        prev=head
                        head =head.next
        else:
            print("No such element found")
    def search(self,data):
        head = self.head
        while head!=None:
            if head.data==data:
                return f"{data} exist"
            head=head.next
        return f"{data} doesn't exist"
ll = SinglyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.print()
print(ll.len())
ll.pop(4)
ll.print()
ll.Insert(5.5,6)
ll.append(7)
ll.append(8)
ll.append(9)
ll.append(10)
ll.print()
print(ll.search(10))
ll.pop(10)
ll.print()
print("tail==> ",ll.tail.data)
