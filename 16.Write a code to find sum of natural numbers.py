def mySum(n) :
    return n*(n+1) // 2
num = int(input("Enter a number : "))
ans = mySum(num)
print(f"The sum is {ans}")
#Way2
"""
    def mySum(a, b) :
    sum = 0
    for i in range(a, b+1) :
        sum += i
    return sum
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

if num1 > 0 and num1 < num2 :
    ans = mySum(num1, num2)
    print(f"The sum between {num1} and {num2} is {ans}")
else :
     print("Enter valid number")
"""