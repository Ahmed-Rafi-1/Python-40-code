def check_empty(list1):
    if not list1:
        return "Given list is empty"
    else:
        return "Given list is not empty"
user_list1 = []
print(check_empty(user_list1))

user_list2 = [1, 2, 3]
print(check_empty(user_list2))