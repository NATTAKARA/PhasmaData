#By Saikuru
#Version 8\5\4
#Phasma Project Data Base
#English Version


import json

print('>>>  Started')

# static command
add_moderator = '~addmod'
add_iventolog = '~addevent'
read_bd = '~readbd'
delete = '~delete_user'
search = '~search'
help = '~help'

#translate



print('Before starting work, familiarize yourself with the guide.')

# Load existing data from mod.json
def load_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return json.load(f)

data = load_data('mod.json')

# Save data to mod.json
def save_data(data, file_name):
    data = json.dumps(data, indent=4)
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(data)

while True:
    command = input('Enter command:  ')

    if command == add_moderator:
        print('You are using the command to add a moderator to the database. ')
        newsmoder_nick = input('nick-name   ')
        newsmoder_id = input('UID   ')
        dol = input('Rang  ')
        new_moder = {'name': newsmoder_nick, 'uid': newsmoder_id, 'rang': dol}
        data['mod'].append(new_moder)
        print('Moderator successfully entered in the database, ')
        save_data(data, 'mod.json')

    elif command == add_iventolog:
        print('You are using the command to add an eventologist to the database. ')
        newsmoder_nick = input('nick-name   ')
        newsmoder_id = input('UID  ')
        dol = input('Rang   ')
        new_iventolog = {'name': newsmoder_nick, 'uid': newsmoder_id, 'rang': dol}
        data['ivent'].append(new_iventolog)
        print('Eventologist successfully entered in the database')
        save_data(data, 'mod.json')


    elif command == read_bd:

        print('Current database of users:')

        print('---------------------------')

        print('Moderators:')

        for i, user in enumerate(data['mod'], 1):
            print(f'{i}. {user["name"]} (UID: {user["uid"]}  - Rang {user["rang"]})')

        print('---------------------------')

        print('Eventologists:')

        for i, user in enumerate(data['ivent'], 1):
            print(f'{i}. {user["name"]} (UID: {user["uid"]}  - Rang {user["rang"]})')

        print('---------------------------')

    elif command == delete:
        print('You are using the command to delete a user from the database')
        namedel = input('Enter UID or name of the user to delete: ')
        found = False
        for user in data['mod']:
            if user['uid'] == namedel or user['name'] == namedel:
                data['mod'].remove(user)
                print(f'User {namedel} successfully deleted from the database')
                found = True
                break
        if not found:
            for user in data['ivent']:
                if user['uid'] == namedel or user['name'] == namedel:
                    data['ivent'].remove(user)
                    print(f'User {namedel} successfully deleted from the database')
                    break
        if not found:
            print(f'User {namedel} not found in the database')
        save_data(data, 'mod.json')

    elif command == search:
        print('You are using the command to search for a user in the database.')
        search_key = input('Enter UID or name of the user to search: ')
        found = False
        for user in data['mod']:
            if user['uid'] == search_key or user['name'] == search_key:
                print(f'User {search_key} found in the database:')
                print(f'Name: {user["name"]}')
                print(f'UID: {user["uid"]}')
                print(f'Rang: {user["rang"]}')
                found = True
                break
        if not found:
            for user in data['ivent']:
                if user['uid'] == search_key or user['name'] == search_key:
                    print(f'User {search_key} found in the database:')
                    print(f'Name: {user["name"]}')
                    print(f'UID: {user["uid"]}')
                    print(f'Rang: {user["rang"]}')
                    found = True
                    break
        if not found:
            print(f'User {search_key} not found in the database')

    elif command == help:
        print('Hello')
        print('Programm by Saikuru, Felix, Natsumi, Freemanisalive')
        print('Command: ')
        print('~addmod - Add moderator to the database')
        print('~addevent - Add an eventologist to the database')
        print('~readbd - Read the database of users')
        print('~delete - Delete a user from the database')
        print('~search - Search a user in the database')
        print('~help - Show this message')
        print('Prefix - ~ ')
        print('Version is DataBase - 8|5|4')
        print('Phasma Project - DataBase')

    else:
        print('Invalid command')
