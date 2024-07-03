
def line():
    print('~'*20)

class Node():

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Stack():

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head == None: #Checking if list is empty
            self.head = new_node #first
            self.tail = new_node #and last
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def pop(self):
        if not self.tail:
            return 'Cant pop from an empty list'
        popped = self.tail
        self.tail = popped.prev
        self.tail.next = None
        return popped.data
    
    def insert(self, idx, data):

        new_node = Node(data)
        current = self.head
        count = 1
        while count < idx:
            current = current.next
            count += 1

        new_node.next = current.next
        new_node.prev = current
        current.next = new_node
        new_node.next.prev = new_node





    


alist = Stack()
alist.append('plain pancake')
alist.append('blueberry pancake')
alist.append('choccy chip pancake')
alist.append('cinnamon roll pancake')

alist.traverse()

print(alist.pop())

line()

alist.traverse()
line()
alist.insert(2, 'peanutbutter pancake')
alist.traverse()