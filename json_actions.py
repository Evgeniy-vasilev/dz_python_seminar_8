import json
import gui


def read_json(path):
    with open(path) as f:
        templates = json.load(f)
    return dict(templates)


def find_json(path):
    user_name = gui.find_contact()
    templates = read_json(path)
    [info, number] = templates[user_name]
    information = f'\
abonent: {user_name} \n\
info: {info} \n\
phonenumber: {number}'
    print(information)
    return information


def write_json(path):
    new_contact = gui.add_contact_json()
    templates = dict(read_json(path))

    templates.update(new_contact)
    with open(path, 'w') as f:
        f.write(json.dumps(templates))
        print('Запись сделана!')


def delete_json(path):
    user = gui.find_contact()
    templates = dict(read_json(path))
    templates.pop(user, None)
    with open(path, 'w') as f:
        f.write(json.dumps(templates))
        print(f'Контакт {user} удален!')


def add_json(path_1, path_2):
    templates_1 = dict(read_json(path_1))
    templates_2 = dict(read_json(path_2))
    templates_1.update(templates_2)

    with open(path_1, 'w') as f:
        f.write(json.dumps(templates_1))
        print('Справочники объединены!')
