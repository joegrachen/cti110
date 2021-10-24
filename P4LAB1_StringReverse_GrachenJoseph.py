user_value = input()

while 1:
    if any(user_value == var for var in ['Done', 'done', 'd']):
        break

    print(''.join(list(reversed(user_value))))
    user_value = input()