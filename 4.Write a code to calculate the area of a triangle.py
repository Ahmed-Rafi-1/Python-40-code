def tri_area(a, b, c):
    if a**2 == int(b**2 + c**2):
        return 0.5*b*c
    else :
        s = (a * b * c) / 2
        return (s*(s-a)*(s-b)*(s-c))**0.5

num1 = int(input("Enter the largest length: "))
num2 = int(input("Enter the second length: "))
num3 = int(input("Enter the third length: "))

result = tri_area(num1, num2, num3)
print(f"The area of the Triangle is {result}")