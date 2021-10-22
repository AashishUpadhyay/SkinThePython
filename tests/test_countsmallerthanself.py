from src.count_smaller_than_self import CountSmallerThanSelf

def test1():
    csts = CountSmallerThanSelf()
    received = csts.count([5,2,6,1])
    expected = [2,1,1,0]
    for i in range(len(received)):
        assert received[i] == expected[i]

def test2():
    csts = CountSmallerThanSelf()
    received = csts.count([8,4,3,6,2,1,11])
    expected = [5,3,2,2,1,0,0]
    for i in range(len(received)):
        assert received[i] == expected[i]

def test3():
    csts = CountSmallerThanSelf()
    received = csts.count([-1])
    expected = [0]
    for i in range(len(received)):
        assert received[i] == expected[i]  

def test4():
    csts = CountSmallerThanSelf()
    received = csts.count([-1, -1])
    expected = [0, 0]
    for i in range(len(received)):
        assert received[i] == expected[i]        

def test5():
    csts = CountSmallerThanSelf()
    received = csts.count([26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41])
    expected = [10,27,10,35,12,22,28,8,19,2,12,2,9,6,12,5,17,9,19,12,14,6,12,5,12,3,0,10,0,7,8,4,0,0,4,3,2,0,1,0]
    for i in range(len(received)):
        assert received[i] == expected[i]

def test6():
    csts = CountSmallerThanSelf()
    received = csts.count([26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41])
    expected = [10,27,10,35,12,22,28,8,19,2,12,2,9,6,12,5,17,9,19,12,14,6,12,5,12,3,0,10,0,7,8,4,0,0,4,3,2,0,1,0]
    for i in range(len(received)):
        assert received[i] == expected[i]

def test7():
    csts = CountSmallerThanSelf()
    received = csts.count([-9361,-750,-8435,-5590,-5835,2958,-3942,-8209,-8241,-9307,7999,9777,-6045,1362,-4022,7045,-1351,9610,-4192,-267,-2120,6657,-9405,-7549,8074,3222,-5563,204,2999,3961,-6798,-53,2349,-6533,-223,1033,7369,-6896,-1756,-127,6161,-7878,9644,2595,-1269,8314,8815,-7448,9973,9797,1802,-6681,6742,-2199,795,6579,2676,9505,-3383,-4465,6993,1317,6608,-8496,-512,-100,5136,686,-2667,1892,-2416,4272,1011,-6260,5780,-2764,-7807,3267,833,-8811,-4751,7541,-2562,5043,-7245,-2427,-6331,147,-2974,759,-2200,-9467,6092,9013,-6563,3810,-4710,-9420,-9173,-7326,1120,-5794,3928,7327,3017,-8873,6524,-7972,-769,-1121,3126,-1586,-2184,-6868,6536,-3325,-9561,-7140,-9483,2271,-6239,-128,6595,-6159,3560,-6865,-8249,1165,5062,-7508,3492,-1801,9877,4857,6104,-7193,9776])
    expected = [5,65,10,37,35,87,42,12,11,5,114,122,31,75,37,107,52,114,36,55,47,100,4,12,103,77,30,57,72,79,21,54,67,23,49,58,90,18,42,48,78,10,90,60,42,84,84,12,88,86,55,18,77,36,47,72,54,77,27,26,71,49,69,7,38,39,59,40,28,44,30,51,40,19,52,26,9,42,36,6,20,52,23,43,10,22,15,28,20,27,20,2,36,41,13,31,16,2,2,6,20,12,25,31,21,2,26,3,15,14,17,13,11,6,19,9,0,4,0,9,4,6,12,4,7,3,0,3,5,0,2,1,4,1,1,0,0]
    for i in range(len(received)):
        assert received[i] == expected[i]

def test8():
    csts = CountSmallerThanSelf()
    received = csts.count([1,3,-1,-3,5,3,6,7])
    expected = [2,2,1,0,1,0,0,0]
    for i in range(len(received)):
        assert received[i] == expected[i]

def test9():
    csts = CountSmallerThanSelf()
    received = csts.count([5,2,6,1,26,78,-1,-1,27,100,8,4,3,6,2,1,11,33,67,90,23,66,5,2,6,1,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,-1,-1,94,13,2,97,3,5,2,6,1,76,99,51,9,21,84,66,65,36,100,41,5,2,6,1])
    expected = [18,9,21,4,33,50,0,0,31,56,23,13,11,16,6,2,19,26,36,42,22,33,10,5,12,2,8,22,12,19,16,22,15,27,19,29,22,24,16,22,15,0,0,20,11,2,18,4,4,2,4,0,11,12,8,4,4,8,7,6,4,5,4,2,1,1,0]
    for i in range(len(received)):
        assert received[i] == expected[i]
