# The password will be considered strong enough if its length is greater than or equal to 10 symbols,
# it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it.


def checkio(data):
    li = list(data)
    a = []
    b = []
    c = []
    for i in li:
        if i.isdigit():
            a.append(int(i))
        if i.isupper():
            b.append(str(i))
        if i.islower():
            c.append(str(i))
    if len(li) < 10:
        return False
    if len(a) >= 1 and len(b) >= 1 and len(c) >= 1:
        return True
    else:
        return False



print(checkio('A1213pokl'))
print(checkio('bAse730onE4'))
print(checkio('asasasasasasasaas'))
print(checkio('QWERTYqwerty'))
print(checkio('123456123456'))
print(checkio('QwErTy911poqqqq'))






