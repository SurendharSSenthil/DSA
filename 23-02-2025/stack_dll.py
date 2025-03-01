# node for doubly linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
#class for stack
class stack:
    def __init__(self):
        self.head = None
        self.tail = None

# push an element into the stack
# time complexity: O(1) -> we are inserting an element into the stack using the tail pointer at constant time.
# space complexity: O(1) -> we are using constant amount of space pushing an element into the stack(ie, new_node).
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

# find the size of teh stack
# time complexity: O(n) -> we are traversing the stack to find the size using the temp pointer.
# space complexity: O(1) -> we are using constant amount of space checking the size of the stack(ie, cnt, temp).
    def size(self):
        cnt = 0
        temp = self.head
        while temp:
            cnt += 1
            temp = temp.next
        return cnt
# pop the top element from the stack
# time complexity: O(1) -> we are popping the top element from the stack using the tail pointer at constant time.It is advantageous over singly linked list implementation since it keeps track of the previous node using prev pointer in each node.
# space complexity: O(1) -> we are using constant amount of space popping an element from the stack(ie, data).
    def pop(self):
        if self.tail is None:
            return None
        if self.head == self.tail:
            data = self.head.data
            self.head = None
            self.tail = None
            return data
        data = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = None
        return data
# top element in the stack
# time complexity: O(1) -> we are returning the top element from the stack using the tail pointer at constant time.
# space complexity: O(1) -> we are using constant amount of space checking the top element of the stack(ie, data).
    def top(self):
        if self.tail is None:
            return None
        return self.tail.data
# check if the stack is empty
# time complexity: O(1) -> we are checking the stack is empty or not using the head pointer at constant time.
# space complexity: O(1) -> we are using constant amount of space
    def is_empty(self):
        return self.head is None
# print the elements of the stack
# time complexity: O(n) -> we are traversing the stack to print the elements using the temp pointer.
# space complexity: O(1)     
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()
def main():
    print("IMplementation of stack using doubly linked list")
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.size()) 
    print(s.peek()) 
    print(s.pop())  
    print(s.pop())  
    print(s.pop())  
    print(s.is_empty()) 
 
if __name__ == "__main__":
    main()