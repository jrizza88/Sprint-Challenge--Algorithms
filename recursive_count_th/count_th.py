'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# ths = "th"

def count_th(word):
    # pass

    if len(word) <= 1:
        # print(f'No th\'s included {0}')
        return 0

    elif word[0] + word[1] == 'th':
        return 1 + count_th(word[1:])
    else: 
        return 0 + count_th(word[1:])




print(count_th(''))
print(count_th('th'))
print(count_th('thtjtjthth'))


