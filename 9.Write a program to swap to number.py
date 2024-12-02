def num_swap(a, b) :
    a,b = b,a
    print(f"After swap a = {a}, b = {b}")

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

print(f"Before swap a = {num1}, b = {num2}")
num_swap(num1, num2)