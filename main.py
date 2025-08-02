students = []

while True:
    try:
        n_students = int(input('Ingrese la cantidad de estudiantes: '))
        if n_students < 1:
            raise Exception('Cantidad inválida.')
    except ValueError:
        print('Debe ser un número entero.\n')
    except Exception as e:
        print('Un error ha ocurrido.', e)
        print()
    else:
        break


for i in range(n_students):
    student = []
    print(f'\nEstudiante #{i+1}')
    name = input('Ingrese el nombre del estudiante: ')
    student.append(name)
    while True:
        try:
            n_grades = int(input('Ingrese la cantidad de notas: '))
            if n_grades < 1:
                raise Exception('Cantidad inválida.')
        except ValueError:
            print('Debe ser un número entero.\n')
        except Exception as e:
            print('Un error ha ocurrido.', e)
            print()
        else:
            break

    grades = []

    for j in range(n_grades):
        print(f'\nNota #{j+1}')
        while True:
            try:
                grade = int(input('Ingrese la nota (0-100): '))
                if grade < 0 or grade > 100:
                    raise Exception('Cantidad fuera de rango.')
                grades.append(grade)
            except ValueError:
                print('Debe ser un número entero.\n')
            except Exception as e:
                print('Un error ha ocurrido.', e)
                print()
            else:
                print('Nota guardada exitosamente')
                break

    student.append(grades)
    students.append(student)

print('\nPROMEDIOS:')
try:
    for i in students:
        print(f'\nEstudiante: {i[0]}')
        sum = 0
        for j in i[1]:
            sum += j
        print(f'Promedio: {round(sum/len(i[1]), 2)}')
except ValueError:
    print('Valor inválido.')
except TypeError:
    print('Operación no válida.')
except ZeroDivisionError:
    print('Divisiones sobre 0 son indefinidas.')
except Exception as e:
    print('Un error ha ocurrido.', e)
