# class for node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#class for stack
class Stack:
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
            self.tail = new_node
    
# size of the stack
# time complexity: O(n) -> we are traversing the stack to find the size using the temp pointer.
# space complexity: O(1) -> we are using constant amount of space checking the size of the stack(ie, cnt, temp).
    def size(self):
        cnt = 0
        temp = self.head
        while temp:
            cnt += 1
            temp = temp.next
        return cnt
# pop the top element from teh stack
# time complexity: O(n) -> we are traversing the stack to find the last element using the temp pointer.
# space complexity: O(1) -> we are using constant amount of space popping an element from the stack(ie, temp).   
    def pop(self):
        if self.tail is None:
            return None
        if self.head == self.tail:
            data = self.head.data
            self.head = None
            self.tail = None
            return data
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        data = self.tail.data
        temp.next = None
        self.tail = temp
        return data
# top element in the stack
# time complexity: O(1) -> we are returning the top element from the stack using the tail pointer at constant time.
# space complexity: O(1) -> we are using constant amount of space returning the top element from the stack(ie, tail). 
    def peek(self):
        if self.tail is None:
            return None
        return self.tail.data
 # check if the stack is empty
# time complexity: O(1) -> we are checking the stack is empty or not using the head pointer at constant time.
# space complexity: O(1) -> we are using constant amount of space.
    def is_empty(self):
        return self.head is None
    
def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.size())
    print(stack.is_empty())
    
if __name__ == '__main__':
    main()