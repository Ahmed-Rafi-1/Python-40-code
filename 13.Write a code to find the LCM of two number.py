def find_gcd(a, b) :
    while b != 0 :
        a,b = b, a%b
    return a
def find_lcm(a,b) :
    return abs(a*b) // find_gcd(a,b)
num1 = int(input("Enter the largest number : "))
num2 = int(input("Enter the other number : "))
print(f"The LCM of {num1} and {num2} is {find_lcm(num1,num2)}")