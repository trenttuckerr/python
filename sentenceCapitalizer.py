'''
Created on Oct 27, 2021

@author: trenttucker
'''

def main():
    user_entry = input('enter sentence to be properly capitalized')
    new = first_cap(user_entry)
    print(new)

def first_cap(inp):
    # sentences = inp.split(". ")
    # sentences2 = [sentence[0].capitalize() + sentence[1:] for sentence in sentences]
    # string2 = '. '.join(sentences2)
    # return string2

    sentences = inp.split('.')
    output = ''
    for i in sentences:
        output = output + i[0].upper() + i[1:] + '.'
    return output

main()