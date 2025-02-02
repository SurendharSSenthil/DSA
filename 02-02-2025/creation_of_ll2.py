class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
# method for creating a linked list from a list of data
# Time complexity is O(n)
# Analysis: for the first element, it takes O(1) time and for the second element, it takes O(1) time and so on. Since we keep track of the last element in the linked list(ie, tail), it takes only O(1) time to add an element to the linked list. And so, for 'n' elements, it takes O(n) time.
# Space Complexity is O(n) since nodes are created for each element in the list.
def create_linked_list(data):
    head = None
    tail = None
    for x in data:
        node = Node(x)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head

def print_linked_list(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' -> ')
        tmp = tmp.next
    print('None')
def main():
    data = [1, 2, 3, 4, 5]
    head = create_linked_list(data)
    print_linked_list(head)
    
if __name__ == '__main__':
    main()