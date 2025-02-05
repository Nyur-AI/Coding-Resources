#Deletion of Particular Node From Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Creating Nodes
head = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

head.next = node2
node2.next = node3
node3.next = node4

current = head
while (current.next is not None) and (current.next.data != 30):
    current = current.next

if current.next is not None:
    current.next = current.next.next

current = head
while current:
    print(current.data, end = " -> ")
    current = current.next
print("None")
