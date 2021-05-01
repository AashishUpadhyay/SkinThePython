from src.arbitraryqueueusingfixedlengtharray import ArbitraryQueueUsingFixedLengthArray


def test_1():
    aqufla = ArbitraryQueueUsingFixedLengthArray(5)

    assert aqufla.enqueue(1) == 1
    assert aqufla.enqueue(2) == 1
    assert aqufla.enqueue(3) == 1
    assert aqufla.dequeue() == 1
    assert aqufla.dequeue() == 2
    assert aqufla.enqueue(4) == 1
    assert aqufla.enqueue(5) == 1
    assert aqufla.enqueue(1) == 1
    assert aqufla.enqueue(1) == 1
    assert aqufla.qsize() == 5
    assert aqufla.dequeue() == 3
    assert aqufla.dequeue() == 4
    assert aqufla.dequeue() == 5
    assert aqufla.dequeue() == 1
    assert aqufla.dequeue() == 1
    assert aqufla.dequeue() == -1
    assert aqufla.enqueue(1) == 1
    assert aqufla.enqueue(2) == 1
    assert aqufla.enqueue(3) == 1
    assert aqufla.enqueue(4) == 1
    assert aqufla.enqueue(5) == 1
    assert aqufla.qsize() == 5
    assert aqufla.dequeue() == 1
    assert aqufla.dequeue() == 2
    assert aqufla.dequeue() == 3
    assert aqufla.dequeue() == 4
    assert aqufla.dequeue() == 5
    assert aqufla.qsize() == 0


def test_2():
    aqufla = ArbitraryQueueUsingFixedLengthArray(5)
    assert aqufla.enqueue(1) == 1
    assert aqufla.enqueue(2) == 1
    assert aqufla.enqueue(3) == 1
    assert aqufla.enqueue(4) == 1
    assert aqufla.enqueue(5) == 1
    assert aqufla.qsize() == 5
    assert aqufla.dequeue() == 1
    assert aqufla.dequeue() == 2
    assert aqufla.dequeue() == 3
    assert aqufla.dequeue() == 4
    assert aqufla.dequeue() == 5
    assert aqufla.qsize() == 0
