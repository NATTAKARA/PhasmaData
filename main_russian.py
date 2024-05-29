#От Saikuru
#Версия 8\5\4
#База данных проекта Фазма
#Русский Перевод
import json
import discord
from discord.ext import commands

print('>>>  Начало работы')

# статическая команда
add_moderator = '~addmod'
add_iventolog = '~addevent'
read_bd = '~readbd'
delete = '~delete_user'
search = '~search'
help = '~help'
logscommands = '~logscommands'
logsmod = '~logsmod'


print('---------------------------------------------------------------')
print('Перед началом работы ознакомьтесь с руководством.')
print('---------------------------------------------------------------')

# Загрузка существующих данных из mod.json
def load_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return json.load(f)

data = load_data('mod.json')

# Сохранение данных в mod.json
def save_data(data, file_name):
    data = json.dumps(data, indent=4)
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(data)

while True:
    command = input('Введите команду:  ')

    if command == add_moderator:
        print('---------------------------------------------------------------')
        print('Вы используете команду для добавления модератора в базу данных.')
        print('--------------------------------------------------------------')
        print('Никнейм: ')
        newsmoder_nick = input('>>> ')
        print('UID: ')
        newsmoder_id = input('>>> ')
        print('Ранг: ')
        dol = input('>>> ')
        new_moder = {'name': newsmoder_nick, 'uid': newsmoder_id, 'rang': dol}

        data['mod'].append(new_moder)
        print('---------------------------------------------------------------')
        print('Модератор успешно добавлен в базу данных, ')
        print('---------------------------------------------------------------')
        save_data(data, 'mod.json')

    elif command == add_iventolog:
        print('---------------------------------------------------------------')
        print('Вы используете команду для добавления ивентолога в базу данных.')
        print('---------------------------------------------------------------')
        print('Никнейм:  ')
        newsmoder_nick = input('>>> ')
        print('UID:  ')
        newsmoder_id = input('>>> ')
        print('Ранг:  ')
        dol = input('>>> ')
        new_iventolog = {'name': newsmoder_nick, 'uid': newsmoder_id, 'rang': dol}
        data['ivent'].append(new_iventolog)
        print('---------------------------------------------------------------')
        print('Ивентолог успешно добавлен в базу данных')
        print('---------------------------------------------------------------')
        save_data(data, 'mod.json')


    elif command == read_bd:

        print('Текущая база данных пользователей:')

        print('---------------------------')

        print('Модераторы:')

        for i, user in enumerate(data['mod'], 1):
            print(f'{i}. {user["name"]} (UID: {user["uid"]}  - Ранг {user["rang"]})')

        print('---------------------------')

        print('Ивентологи:')

        for i, user in enumerate(data['ivent'], 1):
            print(f'{i}. {user["name"]} (UID: {user["uid"]}  - Ранг {user["rang"]})')

        print('---------------------------')

    elif command == delete:
        print('---------------------------------------------------------------')
        print('Вы используете команду для удаления пользователя из базы данных')
        namedel = input('Введите UID или имя пользователя для удаления: ')
        found = False
        for user in data['mod']:
            if user['uid'] == namedel or user['name'] == namedel:
                data['mod'].remove(user)
                print('---------------------------------------------------------------')
                print(f'Пользователь {namedel} успешно удален из базы данных')
                print('---------------------------------------------------------------')
                found = True
                break
        if not found:
            for user in data['ivent']:
                if user['uid'] == namedel or user['name'] == namedel:
                    data['ivent'].remove(user)
                    print('---------------------------------------------------------------')
                    print(f'Пользователь {namedel} успешно удален из базы данных')
                    print('---------------------------------------------------------------')
                    break
        if not found:
            print('---------------------------------------------------------------')
            print(f'Пользователь {namedel} не найден в базе данных')
            print('---------------------------------------------------------------')
        save_data(data, 'mod.json')

    elif command == search:
        print('---------------------------------------------------------------')
        print('Вы используете команду для поиска пользователя в базе данных.')
        print('---------------------------------------------------------------')
        search_key = input('Введите UID или имя пользователя для поиска: ')
        found = False
        for user in data['mod']:
            if user['uid'] == search_key or user['name'] == search_key:
                print(f'Пользователь {search_key} найден в базе данных:')
                print(f'Имя: {user["name"]}')
                print(f'UID: {user["uid"]}')
                print(f'Ранг: {user["rang"]}')
                found = True
                break
        if not found:
            for user in data['ivent']:
                if user['uid'] == search_key or user['name'] == search_key:
                    print(f'Пользователь {search_key} найден в базе данных:')
                    print(f'Имя: {user["name"]}')
                    print(f'UID: {user["uid"]}')
                    print(f'Ранг: {user["rang"]}')
                    found = True
                    break
        if not found:
            print(f'Пользователь {search_key} не найден в базе данных')

    elif command == help:
        print('---------------------------------------------------------------')
        print('Привет')
        print('Программа от Saikuru, Felix, Natsumi, Freemanisalive')
        print('---------------------------------------------------------------')
        print('Команды: ')
        print('~addmod - Добавить модератора в базу данных')
        print('~addevent - Добавить ивентолога в базу данных')
        print('~readbd - Прочитать базу данных пользователей')
        print('~delete - Удалить пользователя из базы данных')
        print('~search - Поиск пользователя в базе данных')
        print('~help - Показать это сообщение')
        print('---------------------------------------------------------------')
        print('Префикс - ~ ')
        print('Версия базы данных - 8|5|4')
        print('Проект Фазма - База данных')

    else:
        print('---------------------------------------------------------------')
        print('Недопустимая команда')
        print('---------------------------------------------------------------')

