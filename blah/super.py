class SimpleList():
    def p(self):
        print("Simple List")

    def p1(self):
        print("Simple p1 List")


class IntList(SimpleList):
    def p(self):
        print("Int List")
        super().p()


class SortedList(SimpleList):
    def p(self):
        print("Sorted List")
        super().p()

    def p1(self):
        print("Sorted p1 List")
        super().p1()


class SomeList(SimpleList):
    def p(self):
        print("Some List")
        super().p()

    def p1(self):
        print("Some p1 List")
        super().p1()


class SortedIntList(IntList, SortedList):
    pass


class SortedPrimeIntList(SortedIntList, SomeList):
    def p(self):
        super().p()
        print("Sorted Int List")

    def p1(self):
        super().p1()
        print("Sorted p1 Int List")
