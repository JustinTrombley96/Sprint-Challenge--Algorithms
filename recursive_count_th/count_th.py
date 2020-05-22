'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# Fibonacci Sequence

def count_th(word):
    target = 'th'
    l = len(word)
    if word == '':
        return 0


    #Attempt 1 (Fails 2 Tests)
    # Multiple and single
    if len(word) < 2:
        return 0
    elif word[0] + word[1] == target:
        return 1 + count_th(word[2:])
    
    return count_th(word[1:])

    #Attempt 2 (Fails 2 Tests)
    # Backwards and multiple
    # return 'th' in word

    #Attempt 3 (Fails 2 Tests)
    # Backwards and multiple
    # if word[0] + word[1] == target:
    #     return 1 
    # return count_th(word[1:])


