import math

def roundup(value, closest_to):
    return ((value//closest_to)*closest_to + closest_to)

def duct_area(Q, v) -> float:
    if v == 0:
       raise ValueError("Velocity cannot be zero.")
    return (Q / v)

def round_duct_dia(area) -> float:
    return (math.sqrt(area*4 / math.pi))

def equivalent_diameter(long_side, short_side):
    eq_dia = (1.3*(long_side*short_side)**0.625 / (long_side+short_side)**0.25)
    return eq_dia

q = 0.4
v = 2
area = duct_area(q,v)

duct_dia = roundup((round_duct_dia(duct_area(q,v))),0.05)

#print(equivalent_diameter(duct_dia, duct_dia-0.05))
print(area)
print(duct_dia * duct_dia-0.05)


#print(equivalent_diameter(0.5,0.4))