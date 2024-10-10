import math

def air_density_and_specific_weight_SI(temperature_C):
    """ Chart header
    Temperature[°C]
    Density[kg/m3]
    Specific weight[N/m3]
    Thermal expansion coefficient[x10-3 K-1]
    """
    chart = [
        [-75,-50,-25,-15,-10,-5,0,5,10,15,20,25,30,40,50,60,80,100,125,150,175,200,225,300,400,500,600,700,800,900,1000,1100],
        [1.783,1.582,1.422,1.367,1.341,1.316,1.292,1.268,1.246,1.225,1.204,1.184,1.164,1.127,1.093,1.060,1.000,0.9467,0.8868,0.8338,0.7868,0.7451,0.7078,0.6168,0.5238,0.4567,0.4043,0.3626,0.3289,0.3009,0.2773,0.2571],
        [17.49,15.52,13.94,13.40,13.15,12.90,12.67,12.44,12.22,12.01,11.81,11.61,11.42,11.06,10.72,10.40,9.81,9.28,8.70,8.18,7.72,7.31,6.94,6.05,5.14,4.48,3.96,3.56,3.23,2.95,2.72,2.52],
        [5.14,4.55,4.08,3.92,3.84,3.76,3.69,3.62,3.56,3.50,3.43,3.38,3.32,3.21,3.12,3.02,2.85,2.70,2.51,2.33,2.22,2.10,2.01,1.76,1.52,1.32,1.16,1.03,0.94,0.86,0.80,0.75]
    ]

def calculate_air_pressure(h):
    """
    Calculate the air pressure of sea level between -500m to 10000m.

    Parameters:
    h (float): Height above sea level in meters.

    Returns:
    float: Air pressure in Pascals.
    """
    if (h < -500) or (h > 10000):
        p0 = 101325  # Sea level standard atmospheric pressure in Pascals
        return p0 * (1 - 2.25577e-5 * h) ** 5.25588
    else:
       raise ValueError("Altitude must between -500m and 10000m.") 

def roundup(value, closest_to):
    return ((value//closest_to)*closest_to + closest_to)

def duct_area(Q, v) -> float:
    if v == 0:
       raise ValueError("Velocity cannot be zero.")
    return (Q / v)

def round_duct_dia(area) -> float:
    return (math.sqrt(area*4 / math.pi))

def equivalent_length(long_side, short_side):
    eq_length = (1.3*(long_side*short_side)**0.625 / (long_side+short_side)**0.25)
    return eq_length

def calculate_reynolds_number(density, velocity, equivalent_length, viscosity):
    """
    Calculate the Reynolds number.

    Parameters:
    density (float): The fluid density (kg/m^3).
    velocity (float): The flow velocity (m/s).
    equivalent_length (float): The equivalent length (m).
    viscosity (float): The dynamic viscosity (Pa.s or N.s/m^2).

    Returns:
    float: The Reynolds number.
    """
    reynolds_number = (density * velocity * equivalent_length) / viscosity
    return reynolds_number

def calculate_hydraulic_diameter_rectangular(height, width):
    """
    Calculate the hydraulic diameter for a rectangular duct.

    Parameters:
    height (float): The height of the duct (m).
    width (float): The width of the duct (m).

    Returns:
    float: The hydraulic diameter (m).
    """
    hydraulic_diameter = 2 * (height * width) / (height + width)
    return hydraulic_diameter

q = 0.4
v = 2
area = duct_area(q,v)

duct_dia = roundup((round_duct_dia(duct_area(q,v))),0.05)

#print(equivalent_length(duct_dia, duct_dia-0.05))
#print(area)
#print(duct_dia * duct_dia-0.05)
calculate_air_pressure(-500)

#print(equivalent_length(0.5,0.4))