#from operator import xor

from sys import stdin
import math
from fractions import Fraction
from fractions import gcd
#pref = []
#arr = []
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


 
T = input()
for i in range(0,int(T)):
    l,d,t = [int(j) for j in input().split()]
    theta = math.acos(d/l)
    print(theta*(180/math.pi))
    print(l*math.cos(t*theta))
    x = Fraction(l*math.cos(t*theta)).limit_denominator()
    #x = Fraction(float(input())).limit_denominator()
    print(str(x.numerator)+" "+str(x.denominator))
    
    r = modinv(x.denominator,1000000007)
    ans = ((x.numerator%1000000007)*(r%1000000007))%1000000007
    if(ans<0):
        ans = ans + 1000000007
    print(ans)
    
