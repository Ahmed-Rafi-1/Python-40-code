def convert_celsius(n) :
    return (n*9/5) + 32
num = float(input("Enter the Temperature in Celsius : "))
result = convert_celsius(num)
print(f"The Temperature in Fahrenheit is {result}")