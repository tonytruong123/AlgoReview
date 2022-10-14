class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    # create a node value, because we insert the node at the beginning
    # the next va
    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        # if the head is blank
        if self.head == None:
            # the head will be the node using the data
            # because we only insert want element => the next element should be none
            self.head = Node(data, None)
            return

        # if the head is not blank
        itr = self.head
        # if the next value is not blank => not at the end
        while itr.next:
            # move to the next value
            itr = itr.next
        # if the next value of the current head is blank => at the end of the linked list
        # then we want to assign that next value to the data
        # since this is the last node => no next node
        itr.next = Node(data, None)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_end(79)
    ll.print()
