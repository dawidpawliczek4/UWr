def split_by_sign(self):
    positive_list = LinkedList()
    negative_list = LinkedList()
    positive_tail = None
    negative_tail = None

    current = self.head
    while current:
        next = current.next 
        current.next = None      

        if current.value >= 0:
            if positive_tail:
                positive_tail.next = current
            else:
                positive_list.head = current
            positive_tail = current
        else:
            if negative_tail:
                negative_tail.next = current
            else:
                negative_list.head = current
            negative_tail = current

        current = next

    return positive_list, negative_list