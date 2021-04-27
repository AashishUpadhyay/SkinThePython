import pprint


class Count4:
    def __init__(self):
        self.arr = [["X" for i in range(6)] for i in range(7)]
        self.moves = ["R", "B"]

    def play(self):

        moveIndex = 0
        while True:
            self.printBoard()
            loc = self.makeMove(self.moves[moveIndex])
            if self.gameOver(loc, self.moves[moveIndex]):
                print(f"Game Over! {self.moves[moveIndex]} wins! Congratulations!")
                self.printBoard()
                break

            moveIndex = 1 if moveIndex == 0 else 0

    def printBoard(self):
        for i in range(len(self.arr)):
            pprint.pprint(self.arr[i])

    def makeMove(self, move):
        print(f"{move} your turn please make a move")
        print("enter row now")
        ri = int(input())
        print("enter col now")
        ci = int(input())
        self.arr[ri][ci] = move
        print("value set")
        return [ri, ci]

    def gameOver(self, loc, move):

        if (
            self.horCnt(loc, move) == 4
            or self.verCnt(loc, move) == 4
            or self.diaCnt(loc, move) == 4
        ):
            return True

    def horCnt(self, loc, move):

        ri = loc[0]
        ci = loc[1]

        index = ci - 1
        cnt = 1
        while index >= 0:
            if self.arr[ri][index] == move:
                cnt += 1
            else:
                break
            index -= 1

        index = ci + 1
        while index < len(self.arr[0]):
            if self.arr[ri][index] == move:
                cnt += 1
            else:
                break
            index += 1

        return cnt

    def verCnt(self, loc, move):

        ri = loc[0]
        ci = loc[1]

        index = ri - 1
        cnt = 1
        while index >= 0:
            if self.arr[index][ci] == move:
                cnt += 1
            else:
                break
            index -= 1

        index = ri + 1
        while index < len(self.arr):
            if self.arr[index][ci] == move:
                cnt += 1
            else:
                break
            index += 1

        return cnt

    def diaCnt(self, loc, move):

        ri = loc[0]
        ci = loc[1]

        rindex = ri - 1
        cindex = ci - 1
        cnt = 1
        while rindex >= 0 and cindex >= 0:
            if self.arr[rindex][cindex] == move:
                cnt += 1
            else:
                break
            rindex -= 1
            cindex -= 1

        rindex = ri + 1
        cindex = ci + 1
        while rindex < len(self.arr) and cindex < len(self.arr[0]):
            if self.arr[rindex][cindex] == move:
                cnt += 1
            else:
                break
            rindex += 1
            cindex += 1

        if cnt > 3:
            return cnt

        rindex = ri - 1
        cindex = ci + 1
        cnt = 1
        while rindex >= 0 and cindex < len(self.arr[0]):
            if self.arr[rindex][cindex] == move:
                cnt += 1
            else:
                break
            rindex -= 1
            cindex += 1

        rindex = ri + 1
        cindex = ci - 1
        while rindex < len(self.arr) and cindex >= 0:
            if self.arr[rindex][cindex] == move:
                cnt += 1
            else:
                break
            rindex += 1
            cindex -= 1

        return cnt
