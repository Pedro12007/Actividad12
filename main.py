students = []

while True:
    try:
        n_students = int(input('Ingrese la cantidad de estudiantes: '))
        break
    except ValueError:
        print('Debe ser un número entero.\n')
    except Exception as e:
        print('Un error ha ocurrido.', e)
        print()


for i in range(n_students):
    student = []
    print(f'\nEstudiante #{i+1}')
    name = input('Ingrese el nombre del usuario: ')
    student.append(name)
    while True:
        try:
            n_grades = int(input('Ingrese la cantidad de notas'))
            break
        except ValueError:
            print('Debe ser un número entero.\n')
        except Exception as e:
            print('Un error ha ocurrido.', e)
            print()
    grades = []
    for j in range(n_grades):
        print(f'\nNota #{j+1}')
        while True:
            try:
                grade = int(input('Ingrese la nota:'))
                grades.append(grade)
                break
            except ValueError:
                print('Debe ser un número entero.\n')
            except Exception as e:
                print('Un error ha ocurrido.', e)
                print()

