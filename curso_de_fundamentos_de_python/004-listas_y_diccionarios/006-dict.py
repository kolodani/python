my_dict = {}
print(type(my_dict))

my_dict = {
    'avion' : "bla bla bla",
    'name' : 'Grover',
    'last_name': 'Cleveland',
    'age': 42
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('age'))
print(my_dict.get('un valor'))

print('avion' in my_dict)
print('otro que no' in my_dict)