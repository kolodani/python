def find_volumen(length = 1, width= 1, depth = 1):
    return length * width * depth, width, 'Hola'

result, width, text = find_volumen(width= 10)

print(result)
print(width)
print(text)