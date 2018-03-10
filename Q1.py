def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    counter = 0
    for i in range(1,len(word)):
        counter = 0
        if i+4>len(word)-1:
            break
        if word[i] == word[i-1]:
            counter += 1
            if word[i+2]==word[i+1]:
                counter += 1
                if word[i+4]==word[i+3]:
                    counter += 1
        if counter == 3:
            break
    if counter==3:
        return True
    else:
        return False

ans = trifeca('aabbcc')
print(ans)
