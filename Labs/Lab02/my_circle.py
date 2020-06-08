PI = 3.14159

radius = 0
radius = input("Enter a radius value for a circle: ")
float_radius = float(radius)
circum = 2 * PI * float_radius

print("The circle's circumference is:")
print(circum)

area = PI * float_radius * float_radius

print("The circle's area is:")
print(area)

double_float_radius = float_radius * 2

double_circum = 2 * PI * double_float_radius
double_area = PI * double_float_radius * double_float_radius

circumtimes = double_circum / circum
areatimes = double_area / area
strcircumtimes = str(circumtimes)
strareatimes = str(areatimes)

print("If the entered radius is doubled, then the Circumference is multiplied by "
      + strcircumtimes + " times and the Area is multiplied by " + strareatimes + " times.")

