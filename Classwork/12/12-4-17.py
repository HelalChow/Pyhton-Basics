def gcd(n1, n2):
    if (n1<n2):
        n1, n2 = n2, n1
    while n2 != 0:
        n1 = n2
        n2 = n1%n2
        if n2 ==0:
            return n1


class Rational:
    def __init__(self, numer, denum =1):
        curr_gcd = gcd(numer, denum)
        self.numer = numer/curr_gcd
        self.denum = denum/curr_gcd
    def __repr__(self):
        return str(self.numer) + '/' + str(self.denum)
    def __add__(self, other):
        denominator = self.denum*other.denum
        numerator = other.denum*self.numer + self.denum*other.numer
        return Rational(numerator, denominator)
    def __eq__(self, other):
        return (self.numer == other.numer) and (self.denum == other.denum)



n1 = Rational(1, 3)
n2 = Rational(3, 7)
n3 = Rational(3, 4)