# https://pt.wikipedia.org/wiki/Blum_Blum_Shub

"""Prime numbers that will build 'm'
retrieved from
http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php

p = (3 mod 4)
"""
P1 = 1000000000547
P2 = 1000000016531


""" Blum Blum Shub class"""
class BBS:
    """ :returns a BlumBlumShub object
    :param seed - seed number
    :param prime1 and prime2 - prime numbers that will generate m
    :param size - number of bits

    'num' is the generated pseudo-random number (initiated as seed)
    """
    def __init__(self, seed, size, prime1=P1, prime2=P2):
        self.seed = seed
        self.m = prime1 * prime2
        self.size = size
        self.num = seed
        self.time = 0
        self.result = ''

    """ :returns result from the formula
    x(n+1) = x(n)² mod M
    """
    def algorithm(self):
        self.num = pow(self.num, 2) % self.m
        return self.num

    """
    runs the algorithm (size - 1) times, each time it runs using 
    the last seed (saved in num), receives the result and appends
    the least significant digit to the result, creating
    a binary result of the desired size.
    It starts with 1 in the beginning (this will make sure
    that the number has 'size' bits)
    
    This method of making sure of the size is based in the implementation
    of Blum-Blum-Shub from Jeremy Kun
    https://jeremykun.com/2016/07/11/the-blum-blum-shub-pseudorandom-generator/
    """
    def calculate(self):
        result = "1"
        for _ in range(self.size - 1):
            rnd = self.algorithm()
            b = rnd % 2
            result += str(b)
        self.num = int(result, 2)
        self.result = result
        return result
