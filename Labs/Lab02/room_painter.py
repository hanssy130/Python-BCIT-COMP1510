COVERAGE = 400/4

length = input("Enter the room's length: ")
width = input("Enter the room's width: ")
height = input("Enter the room's height: ")
coats = input("Enter how many coats you're applying: ")

intlength = int(length)
intwidth = int(width)
intheight = int(height)
intcoats = int(coats)

surface_area = intlength * intwidth * intheight - intheight
coverage_needed = surface_area * intcoats

cans_of_paint_required = coverage_needed / COVERAGE
strcans = str(cans_of_paint_required)
print("The number of cans needed for this project are: " + strcans + ".")

#I'm also considering using what I googled. If I import math, I can use the ceiling function to
#apply to the number of cans so that a more realistic answer is provided, rather than one with a decimal.

