def remove_duplicates(list1):
    # (using set) return list(set(list1))
    unique_list = []
    for i in list1 :
        if i not in unique_list:
            unique_list.append(i)
    return unique_list
list1 = list(map(int, input("Enter the elements by spaces : ").split()))
result = remove_duplicates(list1)
print(f"After removing duplicate from list :  {result}")