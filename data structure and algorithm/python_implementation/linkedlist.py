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
        self.head = Node(value, self.head)
    
    def add_last(self, value):
        # if the list empty
        if self.head is None:
            self.add_first(value)
        else:
            tmp = self.head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = Node(value, None)

    def insert_after(self, key, value):
        pass

    def insert_before(self, key, value):
        pass

    def remove(self, key, value):
        pass

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
