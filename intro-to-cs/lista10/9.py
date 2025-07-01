class ListItem:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Dodanie elementu na koniec kolejki
    def enqueue(self, value):
        new_item = ListItem(value)
        if self.tail is None:  # Jeśli lista jest pusta
            self.head = self.tail = new_item
        else:
            self.tail.next = new_item
            new_item.prev = self.tail
            self.tail = new_item

    # Usunięcie elementu z początku kolejki
    def dequeue(self):
        if self.head is None:  # Jeśli lista jest pusta
            return None
        value = self.head.value
        self.head = self.head.next
        if self.head is None:  # Jeśli lista jest teraz pusta
            self.tail = None
        else:
            self.head.prev = None
        return value

    # Usunięcie elementu z końca listy
    def pop_back(self):
        if self.tail is None:  # Jeśli lista jest pusta
            return None
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail is None:  # Jeśli lista jest teraz pusta
            self.head = None
        else:
            self.tail.next = None
        return value