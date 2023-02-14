import random
countries = ['col', 'mex', 'bol', 'per']

population = { country: random.randint(1, 100) for country in countries }
print(population)

result = { country: population for (country, population) in population.items() if population > 50 }
print(result)

text = 'Hola, soy Grover'
unique = { c : c.upper() for c in text if c in 'aeiou' }
print(unique)