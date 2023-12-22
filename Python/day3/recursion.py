def _reverso(word):
    if len(word) == 0:
        return word
    else:
        return _reverso(word[1:]) + word[0]
print(_reverso("reverse"))


def facto(n):
    if n == 1:
        return 1
    else:
        return n * facto(n-1)
print(facto(5))