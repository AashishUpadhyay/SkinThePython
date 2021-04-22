from src.primegenerator import PrimeGenerator

def testGenerate1():
    pg = PrimeGenerator()
    primes = pg.Generate(11)
    assert 2 in primes
    assert 3 in primes
    assert 5 in primes
    assert 7 in primes
    assert 11 in primes
    assert len(primes) == 5

def testGenerate2():
    pg = PrimeGenerator()
    primes = pg.Generate(13)
    assert 2 in primes
    assert 3 in primes
    assert 5 in primes
    assert 7 in primes
    assert 11 in primes
    assert 13 in primes
    assert len(primes) == 6

def testPrimes():
    pg = PrimeGenerator()
    pgen = pg.Primes()
    assert 2 == next(pgen)
    assert 3 == next(pgen)
    assert 5 == next(pgen)
    assert 7 == next(pgen)
    assert 11 == next(pgen)
    assert 13 == next(pgen)
    assert 17 == next(pgen)
    assert 19 == next(pgen)
    assert 23 == next(pgen)
    assert 29 == next(pgen)
