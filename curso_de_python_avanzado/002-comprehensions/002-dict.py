'''
dict = {}
for i in range(1, 11):
    dict[i] = i * 2

print(dict)

dict_v2 = { i: i * 2 for i in range(1, 11) }
print(dict_v2)

import random
countries = ['col', 'mex', 'bol', 'per']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)

print(population)

population_v2 = { country: random.randint(1, 100) for country in countries }
print(population_v2)
'''

names = ['nico', 'pablo', 'juan']
ages = [28, 30, 25]

print(list(zip(names, ages)))

new_dict = { name: age for (name, age) in zip(names, ages) }
print(new_dict)
