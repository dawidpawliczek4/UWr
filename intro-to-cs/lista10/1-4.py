class ListItem:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    #1
    def append(self, value):
        current = self
        while current.next is not None:
            current = current.next
        current.next = ListItem(value)
    
    #2
    def pop(self):
        if self.next is None:
            return None
        current = self
        while current.next.next is not None:
            current = current.next
        popped_value = current.next.value
        current.next = None
        return popped_value
    
    #3
    def appendList(self, list):
        current = self
        while current.next is not None:
            current = current.next
        current.next = list
    
    #4
    def deleteAll(self, value):
        current = self
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
            else:
                current = current.next