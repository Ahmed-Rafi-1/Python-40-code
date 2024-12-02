import random
def random_generator(a, b) :
    return random.uniform(a,b)

num1 = float(input("Enter a lower bound number : "))
num2 = float(input("Enter a higher bound number : "))

result = random_generator(num1, num2)
print(f"A random number between {num1} and {num2} is {result}")