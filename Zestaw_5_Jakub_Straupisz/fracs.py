from math import gcd

def uproszczenie(frac):
    l, m = frac
    if m < 0:
        l, m = -l, -m
    g = gcd(abs(l), abs(m))
    return [l // g, m // g]

def add_frac(a, b): return uproszczenie([a[0] * b[1] + b[0] * a[1], a[1] * b[1]])
def sub_frac(a, b): return uproszczenie([a[0] * b[1] - b[0] * a[1], a[1] * b[1]])
def mul_frac(a, b): return uproszczenie([a[0] *b[0], a[1] * b[1]])

def div_frac(a, b):
    if b[0] == 0:
        raise ZeroDivisionError("Division by zero is forbidden")
    return uproszczenie([a[0] * b[1], a[1] *b [0]])

def is_positive(frac): return frac[0] * frac[1] > 0
def is_zero(frac): return frac[0] == 0
def cmp_frac(a, b): return (a[0] * b[1] > b[0]* a[1]) - (a[0] * b[1] < b[0] * a[1])
def frac2float(frac): return frac[0] / frac[1]