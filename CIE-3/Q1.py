class DoublyNode: 
    def __init__(self, data): 
        self.data = data 
        self.next = None 
        self.prev = None 

class DoublyLinkedList: 
    def __init__(self): 
        self.head = None 
        self.tail = None 
  
    def insert_at_beginning(self, data): 
        new_node = DoublyNode(data) 
        if self.head is None: 
            self.head = self.tail = new_node 
        else: 
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node 

    def delete_node(self):
        if self.head is None:
            return None
        current = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        del current
        return self.head
    
    def traverse_forward(self): 
        current = self.head 
        while current: 
            print(current.data, end=" <-> " if current.next else "")
            current = current.next 
        print()

dl = DoublyLinkedList()
dl.insert_at_beginning(10)
dl.insert_at_beginning(20)
dl.insert_at_beginning(30)
dl.insert_at_beginning(40)
dl.traverse_forward()
dl.delete_node()
dl.traverse_forward()
