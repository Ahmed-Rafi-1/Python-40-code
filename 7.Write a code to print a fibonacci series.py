def fib_series(n):
    a = 0
    b = 1
    for i in range(n) :
        print(a, end = " ")
        next_term = a + b
        a = b
        b = next_term
    print()

num = int(input("Enter a number : "))
if num <= 0 :
    print("Enter a valid number")
else :
    fib_series(num)
    print(f"is the fibonacci series of {num} length")