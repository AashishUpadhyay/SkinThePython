from src.decodestring import DecodeString

def test1():
    ds = DecodeString()
    assert ds.top_down("1") == 1
    assert ds.top_down("11") == 2
    assert ds.top_down("111") == 3
    assert ds.top_down("1111") == 5
    assert ds.top_down("11111") == 8
    assert ds.top_down("111111") == 13
    assert ds.top_down("12") == 2
    assert ds.top_down("226") == 3
    assert ds.top_down("0") == 0
    assert ds.top_down("06") == 0
    assert ds.top_down("2174") == 3
    assert ds.top_down("1757") == 2
    assert ds.top_down("1757") == 2
    assert ds.top_down("00") == 0
    assert ds.top_down("10") == 1
