#Deletion of Node From Start in Linked List

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

#deleting node from beginning
if head is not None:
    head = head.next #update the head to next node

current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")