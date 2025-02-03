#Deletion of Node From End in Linked List

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

# Deleting the last node
if head is None:
    print("List is empty.")
elif head.next is None:
    # If only one node is present, delete it by making head None
    head = None
else:
    current = head
    while current.next.next is not None:
        current = current.next
    current.next = None  # Removing reference to the last node

# Printing the updated linked list
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")