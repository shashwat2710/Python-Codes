"""Checking program output."""
'''
def index_word(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        print(index,letter)
        if letter == " ":
            result.append(index+1)
    return result
'''
##Implementing generator function
def index_word_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == " ":
            yield index+1

##Calling function
#result =  index_word('Four score and seven years ago…')
result = list(index_word_iter('Four score and seven years ago…'))

print(result)