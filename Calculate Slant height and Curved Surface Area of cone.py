"""
Write a python script that takes the radius and height of the cone
from the user. Calculate its slant height(s), CSA
"""
import math
radius = float(input("Enter the value of radius:"))
height = float(input("Enter the value of height"))
slant_height = math.sqrt(radius**2 + height**2)
print(slant_height)
# Curved surface area of cone = pi * r * slant_height
Curved_Surface_Area = math.pi * radius * slant_height
print(Curved_Surface_Area)

