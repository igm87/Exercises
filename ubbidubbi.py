def ubbi_dubbi(word)->str:
    vowel = 'aeiou'
    result = ''

    for i in list(word):
        if i in vowel:
            result += 'ub' + i
        else:
            result += i
    return result


