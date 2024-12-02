list1 = list(map(int, input("Enter the first list : ").split()))
list2 = list(map(int, input("Enter the second list : ").split()))

unique_element = list(set(list1) & set(list2) )

print(f"The common element is {unique_element}")