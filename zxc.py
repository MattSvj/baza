baze_sotr = {}
id_baze_sotr = 1
baze_otdel = {}
id_baze_otdel = 1
baze_post = {}
id_baze_post = 1
baze_full = {}

while True:
    baze = input('С какой таблицей вы хотите работать: '
                 '\n1. Сотрудники'
                 '\n2. Отделы'
                 '\n3. Должности\n')
    if baze == '1':
        do = input('Что вы хотите сделать:'
                   '\n1. Добавить сотрудника'
                   '\n2. Удалить сотрудника'
                   '\n3. Изменить данные о сотруднике\n')
        if do == '1':
            baze_sotr[id_baze_sotr] = (input('Введите фамилию сотрудника: ') + " " + input('Введите номер телефона: '))
            id_baze_sotr += 1
        elif do == '2':
            name = input('Введите фамилию сотрудника для удаления: ')
            if name in list(map(lambda x: x.split()[0], baze_sotr.values())):
                found = list(filter(lambda x: baze_sotr[x].split()[0] == name, baze_sotr))
                baze_sotr.pop(found[0])
            else:
                print('Вы ввели неверную фамилию')
        elif do == '3':
            name = input('Введите фамилию сотрудника для изменения: ')
            if name in list(map(lambda x: x.split()[0], baze_sotr.values())):
                found = list(filter(lambda x: baze_sotr[x].split()[0] == name, baze_sotr))
                baze_sotr[found[0]] = baze_sotr[found[0]].split()[0] + " " + input('Введите новый номер телефона: ')
            else:
                print('Вы ввели неверную фамилию')
        else:
            print('Вы ввели неверное действие. (1, 2, 3)')
    elif baze == '2':
        do = input('Что вы хотите сделать: '
                   '\n1. Добавить отдел'
                   '\n2. Удалить отдел\n')
        if do == '1':
            work = input('Введите название отдела: ')
            baze_otdel[id_baze_otdel] = work
            id_baze_otdel += 1
        elif do == '2':
            work = input('Введите название отдела: ')
            if work in baze_otdel.values():
                found = list(filter(lambda x: baze_otdel[x] == work, baze_otdel))
                baze_otdel.pop(found[0])
            else:
                print('Вы ввели неверное название отдела')
        else:
            print('Вы ввели неверное действие. (1, 2)')
    elif baze == '3':
        do = input('Что вы хотите сделать: '
                   '\n1. Добавить должность'
                   '\n2. Удалить должность\n')
        if do == '1':
            post = input('Введите название должности: ')
            baze_post[id_baze_post] = post
            id_baze_post += 1
        elif do == '2':
            post = input('Введите название должности: ')
            if post in baze_post.values():
                found = list(filter(lambda x: baze_post[x] == post, baze_post))
                baze_post.pop(found[0])
            else:
                print('Вы ввели неверное название должности')
        else:
            print('Вы ввели неверное действие. (1, 2)')
    elif baze == 'всё':
        break
    else:
        print('Вы ввели неверное значение. (1, 2, 3)')
    print(baze_sotr)
    print(baze_otdel)
    print(baze_post)


def func_full(name, otdel='', post=''):
    found_name = list(filter(lambda x: baze_sotr[x].split()[0] == name, baze_sotr))
    found_otdel = list(filter(lambda x: baze_otdel[x] == otdel, baze_otdel))
    found_post = list(filter(lambda x: baze_post[x] == post, baze_post))
    baze_full[found_name[0]] = [found_otdel[0], found_post[0]]
    print('Пользователь успешно авторизирован.')
    print('Имеющиеся пользователи: ')
    for key in baze_full:
        print(key, baze_full[key])
    return


while True:
    ans = input('Хотите ли вы идентифицировать пользователя? (да, нет): ')
    if ans == 'да':
        print('Доступные пользователи:', ", ".join(list(map(lambda x: baze_sotr[x].split()[0], baze_sotr))))
        name = input('Выбор: ')
        if name not in list(map(lambda x: baze_sotr[x].split()[0], baze_sotr)):
            print('Вы ввели недоступную фамилию.')
            continue
        print('Доступные отделы:', ", ".join(baze_otdel.values()))
        otdel = input('Выбор: ')
        if otdel not in baze_otdel.values():
            print('Вы ввели недоступный отдел.')
            continue
        print('Доступные должности:', ", ".join(baze_post.values()))
        post = input('Выбор: ')
        if post not in baze_post.values():
            print('Вы ввели недоступную должность.')
            continue
        func_full(name, otdel, post)
