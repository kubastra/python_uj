## Wielomiany gęste

Projekt udostępnia klasę Polynomial, która obsługuje podstawowe działania na wielomianach:
- dodawanie,
- odejmowanie,
- mnożenie,
- porównywanie,
- obliczanie wartości wielomianu (schemat Hornera),
- czytelną reprezentację tekstową.

Wielomian jest reprezentowany jako lista współczynników:
[a0, a1, a2, ...]
co oznacza wielomian:
a0 + a1·x + a2·x^2 + ...

Przykład: Polynomial([1, 2, 3])
reprezentuje: 1 + 2x + 3x^2

### Zawartość projektu
- Polynomial.py – implementacja klasy Polynomial
- tests.py – testy jednostkow

### Opis funkcji

__init__
Tworzy wielomian na podstawie listy współczynników i usuwa zbędne zera z końca.

_trim
Usuwa końcowe zera z listy współczynników (żeby stopień był poprawny).

is_zero
Sprawdza, czy wielomian jest zerowy.

degree
Zwraca stopień wielomianu.

__getitem__
Zwraca współczynnik przy potędze.

__add__
Zwraca sumę dwóch wielomianów.

__sub__
Zwraca różnicę dwóch wielomianów.

__mul__
Zwraca iloczyn dwóch wielomianów.

__call__
Oblicza wartość wielomianu w punkcie x (schemat Hornera).

__eq__
Sprawdza, czy dwa wielomiany są równe.

__ne__
Sprawdza, czy dwa wielomiany są różne.

__str__
Zwraca czytelną postać tekstową wielomianu.

### Testy 
Aby uruchomić testy:
- python -m unittest tests.py

### Wymagania
- Python 3.x


###Dodatkowe funkcjonalności

Projekt został rozszerzony o obsługę działań między wielomianem a liczbą:

Obsługiwane są operacje:
- p + liczba
- liczba + p
- p - liczba
- liczba - p
- p * liczba
- liczba * p
- p / liczba

Dzielenie jest dozwolone wyłącznie w postaci:
wielomian / liczba
Próba dzielenia przez zero powoduje zgłoszenie wyjątku ZeroDivisionError.
Implementacja tej funkcjonalności została wykonana bez modyfikowania treści klasy Polynomial – poprzez dopięcie odpowiednich operatorów po definicji klasy.