def strsort(word)->str:
    word = list(word)
    result = [word.pop(0)]
    for i in word:
        if ord(i) > ord(result[-1]):
            result.append(i)
        else:
            temp = result.pop()
            result.insert(-1,i)
            result.append(temp)
    return ''.join(result)

