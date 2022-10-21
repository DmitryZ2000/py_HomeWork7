# Задание в группах: Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
from os import system

def db_init(my_phonebook, my_address):
    yes = True
    id = len(my_phonebook)
    while yes:        
        contact_list = []
        surname = input('Введите Фамилие ')
        contact_list.append(surname)
        name = input('Введите имя ')
        contact_list.append(name)
        phonenumber = input('Введите номер телефона ')
        contact_list.append(phonenumber)
        coment  = input('Введите Комментарий ')
        contact_list.append(coment)
        id += 1
        my_phonebook[id] = contact_list

        address_list = []
        city = input('Введите город ')
        address_list.append(city)
        street = input('Введите улицу ')
        address_list.append(street)
        house = input('Введите дом ')
        address_list.append(house)
        my_address[id] = address_list
        next = input('Еще? Для продолжения введите: Да , Чтобы выййти введите любую клавишу: ')
        print(next.upper())
        if next.upper() =='ДА': 
            yes = True
        else: yes = False

def write_file(my_dic, filename = 'phonebook.txt'):
    with open(filename, 'a') as data:
        for man in my_dic:
            my_dic[man]
            # print(';'.join(my_dic[man]))
            # data.write(';'.join(my_dic[man]) +'\n')
            data.write(';'.join(my_dic[man]))
            data.write('\n')
    return print('Запись выполнена')

def read_file(my_dic, filename = 'phonebook.txt'):
    with open(filename, 'r') as data:
        count = 0
        my_dic = {}
        for line in data:
            
            my_dic[count] = line[:-2].split(';') #Срезом убираем символ перевода строки
            count +=1
    return my_dic

def find_name(my_dic, my_adr, my_key):
    for key in my_dic:
        if key == my_key:
            print(' '.join(my_dic[key]), ' '.join(my_adr[key]))
    return

system('cls')

my_phonebook  = {0 : ['Sername', 'Name', 'Phone Number', 'Comment']}
my_address = {0 : ['City', 'Street', 'House']}

db_init(my_phonebook, my_address) # Ввод базы данных

# my_phonebook = {0 : ['Sername', 'Name', 'Phone Number', 'Comment'], 1: ['Smith', 'John', '1234', 'Good boy'], 2: ['Kuzin', 'Oleg', '9033159001', "He's from Russia"]}
# my_address = {0 : ['City', 'Street', 'House'], 1: ['Moscow', 'Kuznteskaya', '10'], 2: ['Volgograd', 'Titova', '12']}

write_file(my_phonebook, 'phonebook.txt')
write_file(my_address, 'address.txt')

# print(read_file('phonebook.txt'))

looking_key = int(input('Введите ключ в записи: '))
find_name(my_phonebook, my_address, looking_key)
