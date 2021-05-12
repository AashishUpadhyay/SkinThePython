from src.datastructures.linkedlist import LinkedList, LinkedListNode
class LRUCache:
    def __init__(self, size) -> None:
        self._size = size
        self._linked_list = LinkedList()
        self._map = dict()

    def get(self, key):
        if key not in self._map:
            return -1

        return_val = self._map[key].val[1]   
        self._linked_list.remove(self._map[key])
        self._linked_list.add(self._map[key])
        return return_val

    def set(self, key, val):
        if key in self._map:
            self._map[key].val[1] = val
            self._linked_list.remove(self._map[key])
            self._linked_list.add(self._map[key])
            return

        node = LinkedListNode([key,val])

        if len(self._map) < self._size:
            self._map[key] = node
            self._linked_list.add(node)
            return
        
        last_node = self._linked_list.remove_last()
        self._map.pop(last_node.val[0])
        self._linked_list.add(node)
        self._map[key] = node
        return





