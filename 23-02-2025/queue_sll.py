# class for Node -> singly linked lst
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# class for Queue
class Queue:
    def __init__(self):
        self.front = None
        self.end = None
 # enqueue an element into the queue
# time complexity: O(1) -> we are inserting an element into the queue using the end pointer at constant time.
# space complexity: O(1) -> we are using constant amount of space(ie, new_node).   
    def enqueue(self, data):
        if self.front is None:
            self.front = Node(data)
            self.end = self.front
        else:
            new_node = Node(data)
            self.end.next = new_node
            self.end = new_node

# dequeue an element from the queue
# time complexity: O(1) -> we are removing an element from the queue using the front pointer at constant time.
# space complexity: O(1) -> we are using constant amount of space(ie, temp).
    def dequeue(self):
        if self.front is None:
            return None
        else:
            temp = self.front
            self.front = self.front.next
            if self.front is None:
                self.end = None
            return temp.data
# front element of the queue
# time complexity: O(1) -> we are returning the front element from the queue using the front pointer at constant time.
# space complexity: O(1)
    def peek(self):
        if self.front is None:
            return None
        return self.front.data
# size of the queue
# time complexity: O(n) -> we are traversing the queue to find the size using the temp pointer.
# space complexity: O(1) -> we are using constant amount of space(ie, count, temp).
    def size(self):
        count = 0
        temp = self.front
        while temp is not None:
            count += 1
            temp = temp.next
        return count
 # check if the queue is empty
 # time complexity: O(1) -> we are checking if the front pointer is None at constant time.
 # space complexity: O(1)   
    def isEmpty(self):
        return self.front is None
 # print teh queue elements
 # time complexity: O(n) -> we are traversing the queue to print the elements using the temp pointer.
    # space complexity: O(1) -> we are using constant amount of space(ie, temp).   
    def display(self):
        temp = self.front
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print()

def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print('Queue after enqueue:', end=' ')
    queue.display()
    print('Size of queue:', queue.size())
    print('Dequeued element:', queue.dequeue())
    print('Queue after dequeue:', end=' ')
    queue.display()
    print('Peek element:', queue.peek())
    print('Is queue empty?', queue.isEmpty())
    
if __name__ == '__main__':
    main()