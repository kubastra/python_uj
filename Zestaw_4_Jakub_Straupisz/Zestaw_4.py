def Zadanie4_2():

    def make_ruler(n):
        gora = ""
        dol = ""
        for i in range(n + 1):
            gora += "|---"
        gora += "|\n"

        for i in range(n + 1):
            dol += str(i).ljust(4)

        return gora + dol

    def make_grid(rows, cols):
        prostokat = ""
        szerokosc = "+---" * cols + "+\n"
        wysokosc = "|   " * cols + "|\n"

        for _ in range(rows):
            prostokat += szerokosc
            prostokat += wysokosc

        prostokat += szerokosc

        return prostokat

def Zadanie4_3(n):
    wynik = 1

    for i in range(1, n + 1):
        wynik *= i

    return wynik

def Zadanie4_4(n):

    if n <= 0:
        return 0

    elif n == 1:
        return 1

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

def Zadanie4_5():

    def odwracanie_iter(L, left, right):

        while left < right:
            L[left], L[right] = L[right], L[left]
            left += 1
            right -= 1

    def odwracanie_rec(L, left, right):
        if left >= right:
            return

        L[left], L[right] = L[right], L[left]

        odwracanie_rec(L, left + 1, right - 1)

def Zadanie4_6(sequence):
    suma = 0

    for item in sequence:
        if isinstance(item, (list, tuple)):
            suma += Zadanie4_6(item)
        else:
            suma += item

    return suma

def flatten(sequence):
    wynik = []

    for item in sequence:
        if isinstance(item, (list, tuple)):
            wynik.extend(flatten(item))
        else:
            wynik.append(item)

    return wynik

if __name__ == '__main__':
    Zadanie4_2()
