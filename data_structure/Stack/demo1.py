from math import gcd


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    def show(self):
        print(self.num, "/", self.den)
    def gcd(m,n):
        while m%n != 0:
            oldm = m
            oldn = n
            m = oldn
            n = oldm%oldn
        return
    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + \
        self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

print(Fraction(3, 5))
f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
f3 = f1 + f2
print(f3)



class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None
    def getLabel(self):
        return self.label
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)
        self.pinA = None
        self.pinB = None
    def getPinA(self):
        return int(input("Enter Pin A input for gate " + \
        self.getLabel() + "-->"))
    def getPinB(self):
        return int(input("Enter Pin B input for gate " + \
        self.getLabel() + "-->"))

class UnaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)
        self.pin = None
    def getPin(self):
        return int(input("Enter Pin input for gate " + \
        self.getLabel() + "-->"))
class AndGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 or b==1:
            return 1
        else:
            return 0

class NotGate(UnaryGate):
    def __init__(self, n):
        super().__init__(n)
    def performGateLogic(self):
        c = self.getPin()
        if c==0:
            return 1
        elif c==1:
            return 0



if __name__ == '__main__':
    g1 = AndGate("G1")
    print(g1.getOutput())
    g2 = OrGate("G2")
    print(g2.getOutput())
    g3 = NotGate("G3")
    print(g3.getOutput())

