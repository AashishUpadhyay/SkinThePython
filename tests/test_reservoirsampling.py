from copy import deepcopy
from src.reservoirsampling import ReservoirSampling


def test_select_element_at_random():
    rs = ReservoirSampling()
    arr = [11, 2, 13, 234, 225, 36, 17]

    elem_map = {}
    for _, elem in enumerate(arr):
        elem_map[elem] = 0

    for _ in range(1000000):
        pick = rs.select_element_at_random(arr)
        elem_map[pick] += 1
    assert True


def test_select_k_elements_at_random():
    rs = ReservoirSampling()
    arr = [11, 2, 13, 234, 225, 36, 17]

    elem_map = {}
    for _, elem in enumerate(arr):
        elem_map[elem] = 0

    for _ in range(1000000):
        picked_items = rs.select_k_elements_at_random(3, deepcopy(arr))
        for p_i in picked_items:
            elem_map[p_i] += 1

    assert True
