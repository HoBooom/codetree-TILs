class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.node_num=0
    
    def push_front(self,data):
        new_node=Node(data)
        new_node.next=self.head

        if self.head==None:
            self.head=new_node
            self.tail=new_node
            new_node.prev=None
        else:
            self.head.prev=new_node
            self.head=new_node
            new_node.prev=None

        self.node_num+=1

    def push_back(self,data):
        new_node=Node(data)
        new_node.prev=self.tail

        if self.tail==None:
            self.head=new_node
            self.tail=new_node
            new_node.prev=None
        else:
            self.tail.next=new_node
            self.tail=new_node
            new_node.next=None

        self.node_num+=1

    def pop_front(self):
        if self.head==None:
            print("list is empty")
        elif self.head.next==None:
            temp=self.head

            self.head=None
            self.tail=None
            self.node_num=0
            return temp.data
        else:
            temp=self.head
            temp.next.prev=None
            self.head=temp.next
            temp.next=None

            self.node_num-=1
            return temp.data
    
    def pop_back(self):
        if self.tail==None:
            print("list is empty")
        elif self.tail.prev==None:
            temp=self.tail

            self.head=None
            self.tail=None
            self.node_num=0
            return temp.data
        else:
            temp=self.tail
            temp.prev.next=None
            self.tail=temp.prev
            temp.prev=None

            self.node_num-=1
            return temp.data

    def size(self):
        return self.node_num

    def empty(self):
        return self.node_num==0

    def front(self):
        if self.head==None:
            print("list is empty")
        else:
            return self.head.data
            
    def back(self):
        if self.tail==None:
            print("list is empty")
        else:
            return self.tail.data

iter_num=int(input())

dll=DoublyLinkedList()

for i in range(iter_num):
    command=input()
    if "push_back" in command:
        comment, data = command.split()
        dll.push_back(int(data))
    elif "push_front" in command:
        comment, data = command.split()
        dll.push_front(int(data))
    elif "pop_front" in command:
        print(dll.pop_front())
    elif "pop_back" in command:
        print(dll.pop_back())
    elif "front" in command:
        print(dll.front())
    elif "back" in command:
        print(dll.back())
    elif "size" in command:
        print(dll.size())
    elif "empty" in command:
        print(int(dll.empty()))