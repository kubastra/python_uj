#Zadanie 3_1: Pierwsze linie są poprawne, stawianie if bezpośrednio w for jest błędne

#Zadanie 3_2:
#  L = L.sort() zwróci nam none
#  x, y = 1, 2, 3 dwie zmienne a trzy wartosci
# X = 1, 2, 3 ; X[1] = 4 to nie tablica
# X = [1, 2, 3] ; X[3] = 4 out of index
# X = "abc" ; X.append("d") str nie ma append
# L = list(map(pow, range(8))) pow bez argumentów

def Zadanie3_3():
    for i in range(0, 30):
        if i % 3 == 0:
            continue
        print(i)

def Zadanie3_4():

    while 1:
        x = input("Podaj liczbe: ")

        if x == "stop": break

        try:
            x = float(x)
            print(f"Liczba: {x} , {pow(x, 3)}")
        except ValueError:
            print(" !!! Wpisz liczbe, a nie napis !!!")

def Zadanie3_5():
    n = int(input("Podaj dlugosc: "))
    dol =""
    gora =""
    for i in range(n + 1):
        gora += "|---"

    for i in range (n + 1):
        dol += str(i).ljust(4)

    gora += "| \n"

    miarka = gora + dol

    print(miarka)

def Zadanie3_6():
    a = int(input("Podaj szerokosc: "))
    b = int(input("Podaj wysokosc: "))

    szerokosc =  "+---" * a + "+\n"
    wysokosc = "|   " * b + "|\n"

    prostokat = ""
    for i in range(b):
        prostokat += szerokosc
        prostokat += wysokosc

    prostokat += szerokosc
    print(prostokat)

def Zadanie3_8():
    A = [1, 2, 3, 4, 5]
    B = [3, 4, 5, 6, 7]

    wspolne = list(set(A) & (set(B)))
    wszystke = list(set(A) | set(B)) # list(set(A).union(set(B))
    print(wspolne)
    print(wszystke)

def Zadanie3_9():
    sekwencje = [[], [4], (1, 2), [3, 4], (5, 6, 7)]

    suma_el = [sum(seq) for seq in sekwencje]
    print(suma_el)

def Zadanie3_10():
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    liczba = 0

    s = input("Podaj liczbe rzymska: ")
    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            liczba -= roman[s[i]]
        else:
            liczba += roman[s[i]]

    print(liczba)


if __name__ == '__main__':
    Zadanie3_10()