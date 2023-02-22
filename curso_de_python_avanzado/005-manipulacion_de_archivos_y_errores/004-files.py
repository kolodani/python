file = open('curso_de_python_avanzado/005-manipulacion_de_archivos_y_errores/text.txt')
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

for line in file:
    print(line)

file.close()

with open('curso_de_python_avanzado/005-manipulacion_de_archivos_y_errores/text.txt') as file:
    for line in file:
        print(line)