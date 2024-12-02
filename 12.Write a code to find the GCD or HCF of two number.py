def find_gcd(a, b) :
    while b != 0 :
        a,b = b, a%b
    return a
num1 = int(input("Enter the largest number : "))
num2 = int(input("Enter the other number : "))
result = find_gcd(num1, num2)
print(f"The GCD/HCF of {num1} and {num2} is {result}")