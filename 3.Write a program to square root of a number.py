import math
num = int(input("Enter a number "))
result = math.sqrt(num)
print(f"The root of {num} is : {result}")
"""
# Without buildin function
"""
def sqr_root(n):
    if n<0 :
        print("Enter positive number")
    else :
        return n**0.5

num = int(input("Enter a number: "))
result = sqr_root(num)
print(f"Ther root of {num} is : {result}")