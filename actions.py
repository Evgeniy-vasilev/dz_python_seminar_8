import gui


def read_file(path: str):
    with open(path, encoding='utf-8', mode='r') as file:
        print('Ваша телефонная книга: ')
        f = file.read()
        print(f)


def write_in_file(path: str):
    with open(path, encoding='utf-8', mode='a') as file:
        file.write(f'{gui.add_contact()}\n')


def find_in_file(path: str):
    with open(path, encoding='utf-8', mode='r') as file:
        f = file.read().split(';')
        f_name = gui.find_contact()
        for i in f:
            if f_name in i:
                print('Искомый контакт найден!')
                print(i)
                break
        else:
            print('Такого контакта нет!')


def delete_in_file(path: str):
    with open(path, encoding='utf-8', mode='r+') as file:
        f = file.read()
        f = f.split(';')
        f_name = gui.find_contact()
        for i in f:
            if f_name in i:
                f.remove(i)
                print(f'Контакт {f_name} удалён!')
                break
    with open(path, encoding='utf-8', mode='w') as file:
        file.write(';'.join(f))
