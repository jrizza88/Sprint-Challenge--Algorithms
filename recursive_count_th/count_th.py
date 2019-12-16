'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    
    # pass

    if word == "":
        print('word', word)
        print(0)
        return 0

    elif word == "th":
        return 1

    # else: 


    return word


print(count_th(''))
print(count_th('th'))


