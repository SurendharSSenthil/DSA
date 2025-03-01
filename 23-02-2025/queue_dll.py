class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

#class for queue thta follows FIFO rule - First in First Out
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
#method to add an element to the queue
#time complexity: O(1) -> we are inserting an element into the queue using the rear pointer at constant time.
#space complexity: O(1) 
    def enqueue(self, data):
        if self.front is None:
            self.front = Node(data)
            self.rear = self.front
        else:
            new_node = Node(data)
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node
#method to remove an element from the queue
#time complexity: O(1) -> we are removing an element from the queue using the front pointer at constant time.
#space complexity: O(1)
    def dequeue(self):
        if self.front is None:
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        return data
#method to get the front element of the queue
#time complexity: O(1) -> we are returning the front element from the queue using the front pointer at constant time.
#space complexity: O(1)
    def peek(self):
        if self.front is None:
            return None
        return self.front.data

#method to check if the queue is empty
#time complexity: O(1) -> we are checking if the front pointer is None at constant time.
#space complexity: O(1)
    def is_empty(self):
        return self.front is None

#method to print the elements of the queue from front to rear
#time complexity: O(n) -> we are traversing the queue to print the elements using the temp pointer.
#space complexity: O(1)
    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print('Queue after enqueue:')
    queue.display()
    print('Front element is:', queue.peek())
    print('Dequeued element is:', queue.dequeue())
    print('Queue after dequeue:')
    queue.display()
    print('Is queue empty?', queue.is_empty())
    
if __name__ == '__main__':
    main()