def askPassword():
    a = input()
    if a=='qwerty':
        print('Доступ разрешён.')
    else:
        a = input()
        if a=='qwerty':
            print('Доступ разрешён.')
        else:
            a = input()
            if a=='qwerty':
                print('Доступ разрешён.')
            else:
                print('Доступ отказан.')
