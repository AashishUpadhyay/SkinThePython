from src.fixedsizequeue import FixedSizeQueue

def test_1():
    fsq = FixedSizeQueue(5)

    assert fsq.enqueue(1) == 1
    assert fsq.enqueue(2) == 1
    assert fsq.enqueue(3) == 1
    assert fsq.dequeue() == 1
    assert fsq.dequeue() == 2
    assert fsq.enqueue(4) == 1
    assert fsq.enqueue(5) == 1
    assert fsq.enqueue(1) == 1
    assert fsq.enqueue(1) == 1
    assert fsq.qsize() == 5
    assert fsq.dequeue() == 3
    assert fsq.dequeue() == 4
    assert fsq.dequeue() == 5
    assert fsq.dequeue() == 1
    assert fsq.dequeue() == 1
    assert fsq.dequeue() == -1
    assert fsq.enqueue(1) == 1
    assert fsq.enqueue(2) == 1
    assert fsq.enqueue(3) == 1
    assert fsq.enqueue(4) == 1
    assert fsq.enqueue(5) == 1
    assert fsq.qsize() == 5
    assert fsq.dequeue() == 1
    assert fsq.dequeue() == 2
    assert fsq.dequeue() == 3
    assert fsq.dequeue() == 4
    assert fsq.dequeue() == 5
    assert fsq.qsize() == 0

def test_2():
    fsq = FixedSizeQueue(5)
    assert fsq.enqueue(1) == 1
    assert fsq.enqueue(2) == 1
    assert fsq.enqueue(3) == 1
    assert fsq.enqueue(4) == 1
    assert fsq.enqueue(5) == 1
    assert fsq.enqueue(6) == -1
    assert fsq.qsize() == 5
    assert fsq.dequeue() == 1
    assert fsq.dequeue() == 2
    assert fsq.dequeue() == 3
    assert fsq.dequeue() == 4
    assert fsq.dequeue() == 5
    assert fsq.dequeue() == -1
    assert fsq.qsize() == 0



