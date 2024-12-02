keys = ['name', 'age', 'city']
value = ['Rafi', '21', 'CTG']
my_dictionary = dict(map(lambda k,v : (k,v), keys, value))
print(my_dictionary)