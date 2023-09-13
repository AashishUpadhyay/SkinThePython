from src.oops import Animal, Gorilla, Lion


def test_gorilla_walk():
    gor = Gorilla()
    gor.walk()
    assert True


def test_lion_walk():
    lion = Lion()
    lion.walk()
    assert True
