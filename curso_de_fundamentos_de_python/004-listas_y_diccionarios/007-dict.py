person = {
    'name': 'Grover',
    'last_name': 'Cleveland',
    'langs' : ['python', 'javascrit'],
    'age': 55
}

print(person)

person['name'] = 'Gervacio'
person['age'] -= 20
person['langs'].append('rust')
print(person)

del person['last_name']
person.pop('age')
print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())