import math

def calc_cube_volume(s):
    return s ** 3


def  calc_rectangular_prism_volume(l, w, h):
    return l * w * h


def calc_cylinder_volume(r, h):
    return math.pi * r ** 2 * h


def calc_shpere_volume(r):
    return 4/3 * math.pi * r ** 3


print(calc_cube_volume(s=3))
print(calc_rectangular_prism_volume(l=1, w=2, h=3))
print(calc_cylinder_volume(r=1.2, h=4))
print(calc_shpere_volume(r=1.3))
