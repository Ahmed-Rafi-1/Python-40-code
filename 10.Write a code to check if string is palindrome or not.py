def is_palindrome(s) :
    s = s.replace(" ","").replace(",", "").replace(".","").replace("!","").lower()
    return s == s[::-1]

str_in = input("Enter a string to check palindrome : ")
if is_palindrome(str_in):
    print("String is palindrome")
else:
    print("String is not palindrome")