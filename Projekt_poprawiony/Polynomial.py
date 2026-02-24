class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = list(coeffs)
        self._trim()

    def _trim(self):
        while len(self.coeffs) > 1 and self.coeffs[-1] == 0:
            self.coeffs.pop()

    def is_zero(self):
        return all(c == 0 for c in self.coeffs)

    def degree(self):
        if self.is_zero():
            return 0
        return len(self.coeffs) - 1

    def __getitem__(self, power):
        if power < 0:
            raise IndexError("potega musi byc dodatnia")

        if power >= len(self.coeffs): return 0

        return self.coeffs[power]

    def __add__(self, other):
        max_len = max(len(self.coeffs), len(other.coeffs))

        result = []
        for i in range(max_len):
            result.append(self[i] + other[i])

        return Polynomial(result)

    def __sub__(self, other):
        max_len = max(len(self.coeffs), len(other.coeffs))
        result = []
        for i in range(max_len):
            result.append(self[i] - other[i])

        return Polynomial(result)

    def __mul__(self, other):
        if self.is_zero() or other.is_zero():
            return Polynomial([0])
        result = [0] * (len(self.coeffs) + len(other.coeffs) - 1)

        for i, a in enumerate(self.coeffs):
            for j, b in enumerate(other.coeffs):
                result[i + j] += a * b

        return Polynomial(result)

    def __call__(self, x):
        result = 0
        for c in reversed(self.coeffs):
            result = result * x + c
        return result

    def __eq__(self, other):
        return (self - other).is_zero()

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        if self.is_zero():
            return "0"

        terms = []
        for power, coef in enumerate(self.coeffs):
            if coef == 0: continue

            if power == 0: terms.append(str(coef))
            elif power == 1:
                if coef == 1:
                    terms.append("x")
                elif coef == -1:
                    terms.append("-x")
                else:
                    terms.append(f"{coef}x")
            else:
                if coef == 1:
                    terms.append(f"x^{power}")
                elif coef == -1: terms.append(f"-x^{power}")

                else:
                    terms.append(f"{coef}x^{power}")
        return " + ".join(terms).replace("+ -", "- ")

_old_add = Polynomial.__add__
_old_sub = Polynomial.__sub__
_old_mul = Polynomial.__mul__


def _poly_add(self, other):
    if isinstance(other, (int, float)):
        other = Polynomial([other])
    return _old_add(self, other)


def _poly_radd(self, other):
    return self + other


def _poly_sub(self, other):
    if isinstance(other, (int, float)):
        other = Polynomial([other])
    return _old_sub(self, other)


def _poly_rsub(self, other):
    return Polynomial([other]) - self


def _poly_mul(self, other):
    if isinstance(other, (int, float)):
        other = Polynomial([other])
    return _old_mul(self, other)


def _poly_rmul(self, other):
    return self * other


def _poly_truediv(self, other):
    if not isinstance(other, (int, float)):
        return NotImplemented
    if other == 0:
        raise ZeroDivisionError
    return Polynomial([c / other for c in self.coeffs])


Polynomial.__add__ = _poly_add
Polynomial.__radd__ = _poly_radd
Polynomial.__sub__ = _poly_sub
Polynomial.__rsub__ = _poly_rsub
Polynomial.__mul__ = _poly_mul
Polynomial.__rmul__ = _poly_rmul
Polynomial.__truediv__ = _poly_truediv