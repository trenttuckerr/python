'''
Created on Oct 27, 2021

@author: trenttucker
'''

def main():
    user_entry = input('enter sentence to be converted to pig latin')
    pig_result = pig_latin(user_entry)
    print(pig_result)
    
def pig_latin(s):
    words = s.split()
    output = ''
    for i in words:
        if len(i) == 1:
            output += i + 'AY '
        else:
            output += i[1:] + i[0] + 'AY '
    return output

main()