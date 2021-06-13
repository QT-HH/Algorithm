import sys
sys.stdin = open('input.txt')

class Node:
    def __init__(self,data,prev=None,next=None):
        self.prev= prev
        self.data= data
        self.next= next

class DoubleLinkedList:
    def __init__(self,data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self,data):
        if self.head==None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data,prev=node)
            node.next = new
            self.tail = new

    def desc(self):
        node = self.head
        while node:
            print(node.data, end='')
            node = node.next

    def insert_before(self,next_data,new_data):
        if self.head is None:
            self.head = Node(new_data)
            self.tail = self.head
            return True
        else:
            node = self.tail
            while node.data != next_data:
                node = node.prev
                if node==None:
                    return False

            prev_node = node.prev
            new_node = Node(new_data,prev=prev_node,next=node)
            if prev_node:
                prev_node.next = new_node
            else:
                self.head = new_node
            node.prev = new_node
            return True

    def insert_after(self,before_node,new_data):
        if self.head is None:
            self.head = Node(new_data)
            self.tail = self.head
            return True
        else:
            node = self.head
            while node is not before_node:
                node = node.next
                if node is None:
                    return False
            next_node = node.next
            new_node = Node(new_data,prev=node,next=next_node)
            if next_node:
                next_node.prev = new_node
            else:
                self.tail = new_node
            node.next = new_node

    def remove(self, node):
        if self.head is None:
            return
        if node is self.tail:
            
        else:
            prev_node = node.prev
            next_node = node.next

            prev_node.next = next_node
            next_node.prev = prev_node
            return prev_node


input = sys.stdin.readline
T = int(input().rstrip())
for t in range(T):
    M = input().rstrip()
    l_list = DoubleLinkedList(None)
    l_list.head = None
    now = l_list.head
    for i in M:
        if i == '<':
            if now:
                now = now.prev
        elif i == '>':
            if now:
                now = now.next
        elif i == '-':
            now = l_list.remove(now)
        else:
            l_list.insert_after(now, i)

    l_list.desc()