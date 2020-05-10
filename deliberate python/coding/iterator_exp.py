"""
this is the python implementation of linkedinlist
adapt to Tory Lee's tutorial CMUß
add a interator class:

1. __iter__ implements yield
2. Iterator class implements __next__ and __iter__
"""

class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.data
            self.current = self.current.next
            return item

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __iter__(self):
        return self.data
    
    def __next__(self):
        return self.next
    
    def __repr__(self):
        print(f"Node {self.data}")

class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, value):
        # O(1)
        self.head = Node(value, self.head)
    
    def add_last(self, value):
        # if the list empty
        # O(n)
        if self.head is None:
            self.add_first(value)
        else:
            tmp = self.head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = Node(value, None)

    def insert_after(self, key, value):
        tmp = self.head
        while tmp is not None:
            if tmp.data==key:
                tmp.next = Node(value,tmp.next)
                return
            tmp = tmp.next
        print(f"no [{key}] found")
        

    def insert_before(self, key, value):
        if self.head.data==key:
            self.add_first(value)
            return
        
        first_pointer = self.head
        second_pointer = self.head.next

        while second_pointer is not None:
            if second_pointer.data==key:
                first_pointer.next=Node(value,second_pointer)
                return
            second_pointer = second_pointer.next
            first_pointer = first_pointer.next
        print(f"no [{key}] found")

    def __str__(self):
        if self.head is None:
            return "None"
        else:
            repr = ""
            tmp = self.head
            while tmp is not None:
                repr+=str(tmp.data)+"->"
                tmp = tmp.next
            return repr
    
    def __iter__(self):
        return LinkedListIterator(self.head)

    # also works without LinkedListIterator
    # def __iter__(self):
    #     current = self.head
    #     while current is not None:
    #         yield current.data
    #         current = current.next

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add_first(4)
    linked_list.add_first("haha")
    linked_list.add_last("end")
    linked_list.insert_after("haha", "after haha")
    linked_list.insert_after("end", "after end")
    linked_list.insert_after("not found", "after not found")
    linked_list.insert_before("end", "before end")
    linked_list.insert_before("haha", "before haha")
    linked_list.insert_before("not found", "before not found")
    print(linked_list)

    ## try to interate
    for node in linked_list:
        print(node)