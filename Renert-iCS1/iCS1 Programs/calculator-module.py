import math

class Calculator:

    def factorial(self, n):
        """
        Computes the factorial of a given natural number, n, generally.
        """
        self.n = n

        # base case
        if (n == 0):
            return 1
        # impossible case
        elif (n < 1):
            return ("WTF?")
        # general case
        else:
            return n * factorial(n - 1)

    # GCD calculator
    def gcd(self, a, b):
        self.a = a
        self.b = b

        if (b == 0):
            return a
        else:
            return gcd(b, a % b)

    # LCM calculator
    def lcm(self, a, b):
        lcm = (a * b) // gcd(a, b)
        return lcm

    # Roots
    def nth_root(self, a, b):
        return b ** (1/float(a))

    # Powers
    def nth_power(self, a, b):
        return a ** b

    # Logorithms
    def log(self, a, b):
        if (b == 0):
            return math.log(a)
        else:
            return math.log(a, b)
        
    # All the other jazz
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b
    def int_divide(self, a, b):
        return a // b