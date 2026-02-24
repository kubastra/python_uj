from math import gcd


class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        if isinstance(x, float) and y == 1:
            x, y = x.as_integer_ratio()

        if isinstance(y, float):
            temp, temp_y = y.as_integer_ratio()
            x *= temp_y
            y = temp

        if y == 0:
            raise ValueError("Nie mozna dzielic przez 0")

        g = gcd(x, y)
        x //= g
        y //= g

        if y < 0:
            x = -x
            y = -y

        self.x = x
        self.y = y

        self.x = x
        self.y = y


    def __str__(self): # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return f"{self.x}"

        return f"{self.x}/{self.y}"

    def __repr__(self):         # zwraca "Frac(x, y)"
        return f"Frac{self.x, self.y}"

    def _to_frac(self, other):
        if isinstance(other, Frac):
            return other
        if isinstance(other, int):
            return Frac(other)
        if isinstance(other, float):
            return Frac(*other.as_integer_ratio())
        raise ValueError("Blad porownania")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        other = self._to_frac(other)
        return self.x * other.y < other.x * self.y

    def __le__(self, other):
        other = self._to_frac(other)
        return self.x * other.y <= self.y * other.x

    def __add__(self, other):
        other = self._to_frac(other)
        return Frac(self.x * other.y + other.x * self.y, self.y * other.y)

    __radd__ = __add__              # int+frac

    def __sub__(self, other):
        other = self._to_frac(other)
        return Frac(self.x * other.y - other.x * self.y, self.y * other.y)

    def __rsub__(self, other):
        other = self._to_frac(other)
        return other - self

    def __mul__(self, other):   # frac1*frac2, frac*int
        other = self._to_frac(other)
        return Frac(self.x * other.x, self.y * other.y)

    __rmul__ = __mul__              # int*frac

    def __truediv__(self, other):   # frac1/frac2, frac/int, Py3
        other = self._to_frac(other)
        if other.x == 0:
            raise ValueError("dzielenie przez 0")
        return Frac(self.x * other.y, self.y * other.x)

    def __rtruediv__(self, other):   # int/frac, Py3
        other = self._to_frac(other)
        return other / self


    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):        # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):       # odwrotnosc: ~frac
        if self.x == 0:
            raise ValueError("brak odwrotnosci dla 0")
        return Frac(self.y, self.x)

    def __float__(self):        # float(frac)
        return self.x / self.y

    def __hash__(self):
        return hash((self.x, self.y))
