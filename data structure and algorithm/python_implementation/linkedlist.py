# this is the python implementation of linkedinlist
# adapt to Tory Lee's tutorial CMUß
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

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

    def remove(self, key):
        if self.head is None: # empty
            return
        if self.head.data == key:
            self.head = self.head.next
            return

        first_pointer = self.head
        second_pointer = self.head.next
        
        while second_pointer is not None:
            if second_pointer.data == key: # if found
                first_pointer.next = second_pointer.next
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


if __name__ == "__main__":
    linked_list = LinkedList()
    print(linked_list)
    linked_list.add_first(4)
    print(linked_list)
    linked_list.add_first("haha")
    print(linked_list)
    linked_list.add_last("end")
    print(linked_list)
    linked_list.insert_after("haha", "after haha")
    print(linked_list)
    linked_list.insert_after("end", "after end")
    print(linked_list)
    linked_list.insert_after("not found", "after not found")
    print(linked_list)
    linked_list.insert_before("end", "before end")
    print(linked_list)
    linked_list.insert_before("haha", "before haha")
    print(linked_list)
    linked_list.insert_before("not found", "before not found")
    print(linked_list)
    linked_list.remove("after end")
    print(linked_list)
    linked_list.remove("before end")
    print(linked_list)
    linked_list.remove("after haha")
    print(linked_list)
    linked_list.remove("before haha")
    print(linked_list)