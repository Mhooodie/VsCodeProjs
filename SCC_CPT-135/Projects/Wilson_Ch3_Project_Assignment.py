'''Chap 3'''

import math

height = float(input("Enter wall height (feet): \n"))
width = float(input("Enter wall width (feet): \n"))
area = int(height * width)
print(f"Wall area: {area} square feet")

paint_needed = area / 350
print(f"Paint needed: {paint_needed:.6f} gallons")
cans_needed = math.ceil(paint_needed)
print(f"Cans needed: {cans_needed} can(s)")

color = input("\nChoose a color to paint the wall: \n")
color_costs = {'red': 35, 'blue': 25, 'green': 23}
total_cost = cans_needed * color_costs[color]
print(f"Cost of purchasing {color} paint:")
print(f"${total_cost}")
