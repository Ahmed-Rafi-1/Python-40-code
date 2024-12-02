def num_check(n) :
    if n%2 == 0 :
        print(f"{n} is even number")
    else :
        print(f"{n} is a odd number")

num = int(input("Enter a number : "))
num_check(num)