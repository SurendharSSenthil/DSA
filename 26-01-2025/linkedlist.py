class student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.next = None

def main():
    st1 = student('surendhar', '71772217149')
    st2 = student('sakthi', '71772217139')
    st3 = student('bala', '71772217107')
    # Linking nodes
    st1.next = st2
    st2.next = st3
    # Print memory addresses of each student nodes
    print("student 1:" , id(st1) ," -> " , "student 2:" , id(st2) , " -> " , "student 3:" , id(st3))
    # Print memory addresses in the next attributes of each nodes
    print("addresses in the next:")
    print("student 1 next:" , id(st1.next) , " -> " , "student 2 next:" , id(st2.next) , " -> " , "student 3 next:" , id(st3.next))
    
def function():
    print("dummy function address: ")
    print(id(function))

if __name__ == '__main__':
    main()
    function()
