my_dictionary = {'name': 'Rafi', 'age': '21', 'city': 'CTG'}
key_to_check = input("Enter the key that you want to check : ")
if key_to_check in my_dictionary:
    print(f"The key {key_to_check} exists in dictionary")
else:
    print(f"The key {key_to_check} doesn't exists in dictionary")