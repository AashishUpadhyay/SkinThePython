from astarsearch import *
import copy


def testbfs1():
    initstate = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
    es = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    sol = Solution(initstate, es)

    assert 1 == sol.bfs(copy.deepcopy(initstate), 2, 1)


def testbfs2():
    initstate = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
    es = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    sol = Solution(initstate, es)

    assert 2 == sol.bfs(copy.deepcopy(initstate), 1, 1)


def testbfsbruteforce2():
    initstate = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
    es = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    sol = Solution(initstate, es)

    assert 2 == sol.bfsbruteforce(copy.deepcopy(initstate), 1, 1)


def testSolve8by8_1():
    initstate = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
    es = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    sol = Solution(initstate, es)

    assert 2 == sol.Solve8by8()


def testSolve8by8_2():
    initstate = [[1, 2, 3], [4, 5, 6], [8, 7, 0]]
    es = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    sol = Solution(initstate, es)

    assert -1 == sol.Solve8by8()


def testbfs3():
    initstate = [[0, 2, 3], [1, 4, 6], [7, 5, 8]]
    es = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    sol = Solution(initstate, es)

    assert 4 == sol.bfs(copy.deepcopy(initstate), 0, 0)


def testbfsbruteforce3():
    initstate = [[0, 2, 3], [1, 4, 6], [7, 5, 8]]
    es = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    sol = Solution(initstate, es)

    assert 4 == sol.bfsbruteforce(copy.deepcopy(initstate), 0, 0)


def testbfs4():
    initstate = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    es = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    sol = Solution(initstate, es)

    assert 0 == sol.bfs(copy.deepcopy(initstate), 2, 2)


def testbfs6():
    initstate = [[2, 3, 0], [1, 4, 6], [7, 5, 8]]
    es = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    sol = Solution(initstate, es)

    assert 6 == sol.bfs(copy.deepcopy(initstate), 0, 2)


def testSolve8by8_3():
    initstate = [[2, 3, 0], [1, 4, 6], [7, 5, 8]]
    es = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    sol = Solution(initstate, es)

    assert 6 == sol.Solve8by8()
