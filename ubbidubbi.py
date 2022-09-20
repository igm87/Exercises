def ubbi_dubbi(word)->str:
    vowel = 'aeiou'
    result = ''
    for item in range(0,len(word)):
        if word[item] in vowel:
            result += 'ub' + word[item]
        else:
            result += word[item]
    return result


