from random import random


def statecounts(trans_probs, startState, steps):
    trans_matrix = buildTransMatrix(trans_probs)
    result = dict()
    currState = startState

    for i in range(steps):
        if currState not in result:
            result[currState] = 0
        result[currState] += 1
        nextState = findNextState(trans_matrix, currState)
        currState = nextState

    return result


def buildTransMatrix(trans_probs):
    result = dict()

    for i in trans_probs:
        if i[0] not in result:
            result[i[0]] = {}
        if i[1] not in result[i[0]]:
            result[i[0]][i[1]] = 0
        result[i[0]][i[1]] = i[2]

    return result


def findNextState(trans_matrix, currState):
    r = random()
    for state, prob in trans_matrix[currState].items():
        r -= prob
        if r <= 0:
            return state


transProbs = [('a', 'a', .9), ('a', 'b', .075), ('a', 'c', .025), ('b', 'a', .15),
              ('b', 'b', .8), ('b', 'c', .05), ('c', 'a', .25), ('c', 'b', .25), ('c', 'c', .5)]
