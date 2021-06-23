class Animal:
    def __init__(self) -> None:
        pass

    def walk(self):
        print('I am gonna walk')

class Gorilla(Animal):
    def __init__(self) -> None:
        pass

    def walk(self):
        print('using my two legs')
        return super(Gorilla, self).walk()

class Lion(Animal):
    def __init__(self) -> None:
        pass

    def walk(self):
        print('using my four legs')
        return super(Lion, self).walk()