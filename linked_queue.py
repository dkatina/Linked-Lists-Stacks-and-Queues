
def line():
    print('~'*20)


class Node():

    def __init__(self, data):
        self.data = data
        self.next = None


class SongQueue():

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data): #O(1) - Constant
        new_song = Node(data)
        if self.head == None: #is my list empty
            self.head = new_song #new song becomes the first item
            self.tail = new_song #but also the last item [new_song]
        else: #if the list is not empty
            self.tail.next = new_song #find the tail, and set the tail's next to new_song (adding new song to the end)
            self.tail = new_song #assigning the 'tail' title to new_song

    def traverse(self): #O(n) Linear
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def dequeue(self): #Playing a song
        if self.head == None: #Check if queue is empty
            return "Can't dequeue an empty list"
        else:
            removed = self.head #remove the head
            self.head = self.head.next #reassign the title of head to what comes next
            return removed.data #return the severed head

queue = SongQueue()

queue.enqueue('Blue')
queue.enqueue('Talladega')
queue.enqueue('Daylily')
queue.enqueue('Willow')
queue.enqueue('Try')

queue.traverse()

print(queue.dequeue())
line()
queue.traverse()

