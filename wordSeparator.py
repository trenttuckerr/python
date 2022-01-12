'''
Created on Oct 27, 2021

@author: trenttucker
'''

def main():
    user_entry = input('enter a sentence with no spaces')
    spaced_sen = word_sep(user_entry)
    spaced_sen.lstrip()
    print(spaced_sen)
    
def word_sep(sentence):
    output = ''
    for i in sentence:
        if i.islower():
            output += i
        else:
            output += ' ' + i
    return output

main()