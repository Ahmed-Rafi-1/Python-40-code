my_dictionary = {
    'apple': '5',
    'samsung': '2',
    'MI': '1',
    'IQOO': '4',
    'Vivo': '7'
}
sorted_dictionary = dict(sorted(my_dictionary.items(), key= lambda item: item[1], reverse=False))
print("Sorted Dictionary is ", sorted_dictionary)