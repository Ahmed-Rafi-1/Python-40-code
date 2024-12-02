def vowel_finder(str) :
    vowel = "aeiouAEIOU"
    count = 0
    for i in str :
        if i in vowel :
            count += 1
    return count
myStr = input("Enter the string here : ")
result = vowel_finder(myStr)
print(f"The number of vowel in string is {result}")