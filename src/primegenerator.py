import heapq
import math


class PrimeGenerator:
    def Generate(self, n):
        s = []
        for i in range(2, n + 1):
            isPrime = True
            for j in range(2, int(math.sqrt(n)) + 1):
                if i != j and i % j == 0:
                    isPrime = False

            if isPrime:
                s.append(i)
        return s

    def Primes(self):
        # i = 2, 3, 4, 5, 6
        # h = 4, 6, 6, 8

        i = 2
        composite = []
        while True:
            if composite and i == composite[0][0]:
                while i == composite[0][0]:
                    popped = heapq.heappop(composite)
                    heapq.heappush(composite, (i + popped[1], popped[1]))
            else:
                heapq.heappush(composite, (i ** 2, i))
                yield i

            i += 1
