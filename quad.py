import math
a = float(input("enter coefficient of a:"))
b = float(input("enter coefficient of b:"))
c = float(input("enter coefficient of c"))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant))/(2*a)
    root2 = (-b - math.sqrt(discriminant))/(2*a)
    print(root1)
    print(root2)
elif discriminant == 0:
    root = -b/(2*a)
    print(root)
else:
    real_part = -b/(2*a)
    imaginary_part = math.sqrt(abs(discriminant))/(2*a)
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")


