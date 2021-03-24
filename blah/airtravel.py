class Flight:

    def __init__(self, number, aircraft):

        if not (number[:2].isalpha()):
            raise ValueError(f"Invalid flight no : {number[:2]}")

        if not (number[:2].isupper()):
            raise ValueError(f"Invalid flight no : {number[:2]}")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route no : {number[2:]}")

        self._number = number
        self._aircraft = aircraft
        rows, seats = aircraft.seating_plan()
        self._seating = [None] + [{s: None for s in seats} for _ in rows]

    def number(self):
        return self._number

    def model(self):
        return self._aircraft.model()

    def allocate_seat(self, seat, passenger):
        row, col = self._parse_seat(seat)

        if not (self._seating[row][col] is None):
            raise ValueError(f"Seat is occupied!")

        self._seating[row][col] = passenger

    def reallocate_seat(self, from_seat, to_seat):
        from_row, from_col = self._parse_seat(from_seat)
        to_row, to_col = self._parse_seat(to_seat)

        if (self._seating[from_row][from_col] is None):
            raise ValueError(f"Seat is empty!")

        if not (self._seating[to_row][to_col] is None):
            raise ValueError(f"Seat is occupied!")

        self._seating[to_row][to_col] = self._seating[from_row][from_col]
        self._seating[from_row][from_col] = None

    def _parse_seat(self, seat):
        rows, seats = self._aircraft.seating_plan()

        if not (seat[-1] in seats):
            raise ValueError(f"Invalid seat no {seat[-1]}")

        try:
            row = int(seat[: -1])
        except ValueError:
            raise ValueError(f"Invalid row no {seat[:-1]}")

        if not (row in rows):
            raise ValueError(f"Invalid row no {seat[:-1]}")

        return (row, seat[-1])

    def available_seats(self):
        return sum(sum(1 for v in row.values() if v is None)
                   for row in self._seating
                   if row is not None)


class Aircraft:

    def __init__(self, reg):
        self._reg = reg

    def registration(self):
        return self._reg

    def num_seats(self):
        rows, cols = self.seating_plan()
        return len(rows) * len(cols)


class Airbus(Aircraft):

    def model(self):
        return "Airbus"

    def seating_plan(self):
        return (range(1, 31), "ABCDEFGHJK"[: 6])


class Boeing(Aircraft):

    def model(self):
        return "Boeing"

    def seating_plan(self):
        return (range(1, 60 + 1), "ABCDEFGHJKLM"[: 12])


def make_flights():
    a = Flight("AA101", Airbus("QWERTY"))
    b = Flight("BB101", Boeing("POIUY"))
    return a, b
