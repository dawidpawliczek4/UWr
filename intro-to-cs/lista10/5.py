class ListItem:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        # pierwszy element listy
        self.head = None
        # ostatni element listy
        self.tail = None

    def append(self, value):
        new_item = ListItem(value)
        if self.tail is None:
            self.head = self.tail = new_item
        else:
            self.tai=l.next = new_item
            self.tail = new_item

    def prepend(self, value):
        new_item = ListItem(value)
        if self.head is None:
            self.head = self.tail = new_item
        else:
            new_item.next = self.head
            self.head = new_item

    def pop_front(self):
        if self.head is None:
            return
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return    