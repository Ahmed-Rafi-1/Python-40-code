def prime_check(n):
    if n<0 :
        print("Enter a valid number")
    else :
        for i in range(2, int(n**0.5) + 1) :
            if n % i == 0 :
                return False
            else :
                return True

num = int(input("Enter a number : "))

if prime_check(num) :
    print(f"{num} is prime number")
else :
    print(f"{num} is not prime number")