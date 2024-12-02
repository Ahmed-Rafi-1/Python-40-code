list1 = list(map(int, input("Enter the elementes of the list : ").split()))
unique_element = {}
for i in list1:
    if i in unique_element:
        unique_element[i] += 1
    else:
        unique_element[i] = 1

for i, count in unique_element.items():
    print(f"Element {i} occurre {count} times")