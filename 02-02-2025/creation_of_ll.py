# definition of class Node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# method for adding a new node at the end of the linked list
# if the head is None, it returns the new_node
# otherwise, it traverses the linked list and adds the new_node at the end which makes the compute time to be O(n).
# Space complexity is O(1) since it uses only a constant amount of space. ie, tmp
def add_to_end(head, new_node):
    if head is None:
        return new_node
    tmp = head
    while tmp.next:
        tmp = tmp.next
    tmp.next = new_node
    return head

# method for printing the linked list
# it traverses the linked list and prints the data of each node
# Time complexity is O(n) since it traverses the entire linked list for printing the data of each node.
# Space complexity is O(1) since it uses only a constant amount of space. ie, tmp
def print_linked_list(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' -> ')
        tmp = tmp.next
    print('None')
    
# method for creating a linked list from a list of data
# Time complexity is O(n^2) 
# Analysis: add_to_end method has a time complexity of O(n) and it is called n times in this method. 
# for the first element, it takes O(1) time and for the second element, it takes O(2) time and so on.
# 1 + 2 + 3 + ... + n = n(n+1)/2 <= O(n^2) ie, Upper Bound Limit
# Space Complexity is O(n) since nodes are created for each element in the list.
def create_linked_list(data):
    head = None
    for x in data:
        node = Node(x)
        head = add_to_end(head, node)
    return head

def main():
    data = [1, 2, 3, 4, 5]
    head = create_linked_list(data)
    print_linked_list(head)

if __name__ == '__main__':
    main()