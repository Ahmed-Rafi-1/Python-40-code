my_dictionary = {'name': 'Rafi', 'age': '21', 'city': 'CTG'}
key_to_remove = input("Enter the key that you have to remove : ")
if key_to_remove in my_dictionary:
    value = my_dictionary.pop(key_to_remove)
    print(f"The key {key_to_remove} is removed from the dictionary with the value {value}")
    print(f"Updated dictionary is {my_dictionary}")
else:
    print(f"The key {key_to_remove} doesn't exists in dictionary")