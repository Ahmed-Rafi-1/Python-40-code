def most_freq(lst):
    if not lst:
        return  None
    frequency = {}
    for i in lst:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    most_frequency = max(frequency, key=frequency.get)
    return most_frequency
my_list = list(map(int, input("Enter the element : ").split()))
result = most_freq(my_list)
print("The frequency element is : ", result)