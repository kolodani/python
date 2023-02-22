with open('curso_de_python_avanzado/005-manipulacion_de_archivos_y_errores/text.txt', 'w+') as file:
    for line in file:
        print(line)
    file.write('nuevas cosas en este archivo\n')
    file.write('otra linea\n')
    file.write('mas linea\n')
