from src.datastructures.linkedlist import LinkedList, LinkedListNode


def test_add_to_empty():
    node = LinkedListNode(1)

    linked_list = LinkedList()
    linked_list.add(node)

    assert linked_list.size == 1
    assert linked_list._head.val == 1
    assert linked_list._tail.val == 1


def test_add_more_than_one_items_to_empty():
    node1 = LinkedListNode(1)
    node2 = LinkedListNode(2)
    node3 = LinkedListNode(3)

    linked_list = LinkedList()
    linked_list.add(node1)
    linked_list.add(node2)
    linked_list.add(node3)

    assert linked_list.size == 3
    assert linked_list._head.val == 3
    assert linked_list._tail.val == 1


def test_remove_last_till_empty():
    node1 = LinkedListNode(1)
    node2 = LinkedListNode(2)
    node3 = LinkedListNode(3)

    linked_list = LinkedList()
    linked_list.add(node1)
    linked_list.add(node2)
    linked_list.add(node3)

    assert linked_list.size == 3
    assert linked_list._head.val == 3
    assert linked_list._tail.val == 1

    assert linked_list.remove_last().val == 1
    assert linked_list.remove_last().val == 2
    assert linked_list.remove_last().val == 3
    assert linked_list.size == 0
    assert linked_list.remove_last() == None


def test_remove():
    node1 = LinkedListNode(1)
    node2 = LinkedListNode(2)
    node3 = LinkedListNode(3)

    linked_list = LinkedList()
    linked_list.add(node1)
    linked_list.add(node2)
    linked_list.add(node3)

    assert linked_list.size == 3
    assert linked_list._head.val == 3
    assert linked_list._tail.val == 1

    linked_list.remove(node2)
    assert linked_list.size == 2
    linked_list.remove(node3)
    assert linked_list.size == 1
    linked_list.remove(node1)
    assert linked_list.size == 0
