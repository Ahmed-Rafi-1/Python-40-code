def freq_check(input_string):
    frequency = {}
    for char in input_string:
        if char!=' ':
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency
input_string = input("Enter a string : ")
frequency_count = freq_check(input_string)
print("Character frequency : ", frequency_count)