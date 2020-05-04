import math
a = ('square')
print(a)
l = int(input('length'))
def area_Square(l):
    area = l ** 2
    return area
print('the area of a square with length {}is {}'.format(l, area_Square(l)))

a = ('rectangle')
print(a)
l = int(input('length'))
b = int(input('breadth'))
def area_Rectangle(l, b):
    area = l * b
    return area
print('the area of a rectangle with length {} and breadth {} is {}'.format(l, b, area_Rectangle(l, b)))

a = ('triangle')
print(a)
b = int(input('base'))
h = int(input('height'))
def area_triangle(b, h):
    area = 1/2 * b * h
    area = round(area, 2)
    return area
print('the area of a triangle with base {} and height {} is {}'.format(b, h, area_triangle(b, h)))

a = ('trapezoid')
print(a)
b1 = int(input('base 1'))
b2 = int(input('base 2'))
h = int(input('height '))
def area_trapezoid(b1, b2, h):
    area = 1/2 * (b1 + b2) * h
    area = round(area, 2)
    return area
print('the area of a trapezoid with base {} and {} and height {} is {}'.format(b1, b2, h, area_trapezoid(b1, b2, h)))

a = ('circle')
print(a)
r = int(input('radius'))
def area_Circle(r):
    area = math.pi * r ** 2
    area = round(area, 2)
    return area
print('the area of a circle with radius {} is {}'.format(r, area_Circle(r)))

a = ('circumfrence of circle')
print(a)
r = int(input('radius'))
def circumfrence_of_circle(r):
    circumfrence = 2 * math.pi * r
    circumfrence = round(circumfrence, 2)
    return circumfrence
print('the circumfrence of circle with radius {} is {}'.format(r, circumfrence_of_circle(r)))

a = ('surface area of cube')
print(a)
a = int(input('length'))
def surface_area_of_cube(a):
    area = 6 * a ** 2
    return area
print('the surface area of cube with length {} is {}'.format(a, surface_area_of_cube(a)))

a = ('curved area of a cylinder')
print(a)
r = int(input('radius 1'))
h = int(input('height '))
def curved_area_of_a_cylinder(r, h):
    area = 2 * math.pi * r * h
    area = round(area, 2)
    return area
print('the curved area of a cylinder with radius {} and height {} is {}'.format(r, h, curved_area_of_a_cylinder(r, h)))

a = ('total surface area of a cylinder')
print(a)
r = int(input('radius 1'))
h = int(input('height '))
def total_surface_area_of_a_cylinder(r, h):
    area = 2 * math.pi * r * (r + h)
    area = round(area, 2)
    return area
print('the total surface area of a cylinder with radius {} and height {} is {}'.format(r, h, total_surface_area_of_a_cylinder(r, h)))

a = ('volume of a cylinder')
print(a)
r = int(input('radius 1'))
h = int(input('height '))
def volume_of_a_cylinder(r, h):
    area = math.pi * r ** 2 * h
    area = round(area, 2)
    return area
print('the volume of a cylinder with radius {} and height {} is {}'.format(r, h, volume_of_a_cylinder(r, h)))

a = ('acceleration')
print(a)
v = int(input('final velocity'))
u = int(input('initial velocity'))
t = int(input('time'))
def acceleration(v, u, t):
    a = (v - u) / t
    a = round(a, 2)
    return a
print('the acceleration of a body is {}'.format(acceleration(v, u, t)))

a = ('density')
print(a)
m = int(input('mass'))
v = int(input('velocity'))
def density(m, v):
    p = m / v
    p = round(p, 2)
    return p
print('the density of an object with mass {} and velocity {} is {}'.format(m, v, density(m, v)))

a = ('pressure')
print(a)
f = int(input('force applied'))
a = int(input('area'))
def pressure(f, a):
    p = f / a
    p = round(p, 2)
    return p
print('the pressure of an object {}'.format(pressure(f, a)))

a = ('kinetic energy')
print(a)
m = int(input('mass'))
v = int(input('velocity'))
def kinetic_energy(m, v):
    e = 1 / 2 * m * v ** 2
    e = round(e, 2)
    return e
print('the kinetic energy is {}'.format(kinetic_energy(m, v)))

a = ('voltage')
print(a)
i = int(input('current'))
r = int(input('resistance in ohms'))
def voltage(i, r):
    v = i * r
    v = round(v, 2)
    return v
print('the voltage is {}'.format(voltage(i, r)))