from src.quack import Quack


def test_1():
    quack = Quack()

    quack.push(1)
    quack.push(2)
    quack.push(3)
    quack.push(4)
    quack.push(5)
    quack.push(6)

    assert quack.pop() == 6
    assert quack.pull() == 1
    assert quack.pull() == 2

    quack.push(7)
    quack.push(8)

    assert quack.pop() == 8
    assert quack.pop() == 7

    assert quack.pull() == 3
    assert quack.pull() == 4
    assert quack.pull() == 5
    assert quack.pull() == -1
    assert quack.pop() == -1
