import string
def punctuation_delete(s) :
    translator = s.maketrans('','',string.punctuation)
    return s.translate(translator)
myStr = input("Enter the string here : ")
print(f"String without punctuation is : {punctuation_delete(myStr)}")