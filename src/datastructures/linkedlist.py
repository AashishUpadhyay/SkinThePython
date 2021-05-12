class LinkedListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self.size = 0

    def add(self, node):
        if self.size == 0:
            self._head = node
            self._tail = node
        else:
            node.next = self._head
            node.next.prev = node    
            self._head = node

        self.size +=1        
        return

    def remove_last(self):
        if self.size == 0:
            return None

        return_val = self._tail   
        self.remove(self._tail)
        return return_val

    def remove(self, node):
        if node == self._head:
            self._head = node.next

        if node == self._tail:
            self._tail = node.prev    

        if node.prev:
            node.prev.next = node.next    

        if node.next:
            node.next.prev = node.prev

        self.size-=1    


  
