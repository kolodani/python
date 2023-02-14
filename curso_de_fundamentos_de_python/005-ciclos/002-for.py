'''
for element in range(1, 21):
    print(element)
'''

my_list = [23, 45, 67, 89, 43]
for element in my_list:
    print(element)

my_tuple = ('nico', 'juli', 'santi')
for element in my_tuple:
    print(element)

product = {
    'name': 'Camisa',
    'price': 100,
    'stock': 89
}

for key in product:
    print(key, '=>', product[key])

for key, value in product.items():
    print(key, '=>', value)

people = [
    {
        'name': 'Nico',
        'age': 34
    },
    {
        'name': 'Juli',
        'age': 45
    },
    {
        'name': 'Santi',
        'age': 5
    }
]

for person in people:
    print('name =>', person['name'])