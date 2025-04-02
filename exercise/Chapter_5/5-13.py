phi = 3.14

def cube(s):
    return s ** 3

def lect(l, w, h):
    return l * w * h

def scorn(r, h):
    return phi * r ** 2 * h / 3

def sphere(r):
    return r ** 3 * 4 / 3

def sylin(r, h):
    return phi * r ** 2 * h

print(cube(12))
print(cube(20))
print(lect(3, 5, 6))
print(f"{scorn(20, 10):.1f}")
print(sphere(15))
print(sylin(20, 10))