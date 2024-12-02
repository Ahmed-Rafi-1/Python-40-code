num = int(input("Enter a number here : "))
rev_number = 0
while num != 0 :
    lastDigit = num % 10
    rev_number = (rev_number * 10) + lastDigit
    num = num // 10

print(f"The reversed number is : {rev_number}")