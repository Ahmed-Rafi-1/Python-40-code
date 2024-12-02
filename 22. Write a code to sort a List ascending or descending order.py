number_list = list(map(int, input("Enter the number seperated by space :").split()))

number_list.sort()
# for reversed order
#number_list.sort(reverse=True)
print(f"Sorted list is {number_list}")