try:
    print(0/0)
    assert 1 != 1, 'Uno no es igual que uno'
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
    print('Error:', error)
except AssertionError as error:
    print('Error:', error)
except Exception as error:
    print('Error:', error)

print('Hola')
