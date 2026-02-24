import random

def zero_one():
    while True:
        yield 0
        yield 1

def random_direction():
    directions = ("N", "E", "S", "W")
    while True:
        yield random.choice(directions)

def week_days():
    while True:
        for day in range(7):
            yield day

if __name__ == "__main__":
    it = zero_one()
    it2 = random_direction()
    it3 = week_days()

    for _ in range(6):
        print(next(it), end=" ")  
        #print(next(it2), end=" ")
        #print(next(it3), end=" ")