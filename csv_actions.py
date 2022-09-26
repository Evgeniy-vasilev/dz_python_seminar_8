import csv
import gui


def write_csv(path):
    with open(path, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(gui.add_contact_csv())
        print('Контакт добавлен!')


def read_csv(path):
    with open(path, newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            print(row)


def find_csv(path):
    f_name = gui.find_contact()
    with open(path, 'rt') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if f_name in row:
                print(f'Искомый контакт: {row}')
                break
        else:
            print('Такого контакта нет!')


def delete_csv(path):
    f_name = gui.find_contact()
    with open(path, newline='') as file:
        reader = csv.reader(file, delimiter=',')
        lst = []
        for row in reader:
            if row[0] != f_name:
                lst.append(row)
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(lst)
        print('Контакт удален!')
