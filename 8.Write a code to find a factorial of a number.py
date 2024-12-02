def num_factorial(n) :
    result = 1
    for i in range(1, n+1) :
        result *= i
    return result
num = int(input("Enter a number : "))
if num <= 0 :
    print("Enter a valid number")
else :
    print(f"The factorial of {num} is {num_factorial(num)}")