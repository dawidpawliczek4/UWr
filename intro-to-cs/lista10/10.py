def merge(self, other):
    #spr czy jakas lista jest pusta
    if self.head is None:
        return other
    if other.head is None:
        return self
    
    # porownojemy pierwsze el obu list(head), ustawiamy merged_head na mniejszy
    if self.head.value < other.head.value:
        merged_head = self.head
        self.head = self.head.next
    else:
        merged_head = other.head
        other.head = other.head.next

    current = merged_head

    # porownujemy kolejne el obu list, ustawiamy current.next na mniejszy
    while self.head is not None and other.head is not None:
        if self.head.value < other.head.value:
            current.next = self.head
            self.head.prev = current
            self.head = self.head.next
        else:
            current.next = other.head
            other.head.prev = current
            other.head = other.head.next
        current = current.next

    if self.head is not None:
        current.next = self.head
        self.head.prev = current
    elif other.head is not None:
        current.next = other.head
        other.head.prev = current

    self.head = merged_head
    while current.next is not None:
        current = current.next
    self.tail = current