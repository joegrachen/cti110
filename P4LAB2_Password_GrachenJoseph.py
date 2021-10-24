pwd = input('')

_key = {'i':'1', 'a':'@', 'm':'M', 'B':'8', 's':'$'}

for letter in pwd:
    if letter in _key.keys():
        i = list(_key.keys()).index(letter)
        pwd = pwd.replace(letter, list(_key.values())[i])

print(pwd + '!')