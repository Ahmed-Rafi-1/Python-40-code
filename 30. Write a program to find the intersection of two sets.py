def find_intersection(set1, set2):
    set_intersection = set1.intersection(set2)
    return set_intersection
set1_input = input("Enter the element fo first set by space : ")
set2_input = input("Enter the element fo second set by space : ")

set1 = set(map(int, set1_input.split()))
set2 = set(map(int, set2_input.split()))

result = find_intersection(set1, set2)
print("Intersection of set1 and set2 : ", result)