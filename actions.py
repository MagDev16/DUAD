def add_students(students):
    n = int(input("Cuantos estudiantes desea ingresar? "))
    for _ in range(n):
        student = {}
        print(f"\nIngrese los datos del estudiante {len(students) + 1}:")

        student["nombre"] = input("Nombre completo: ")
        student["seccion"] = input("Seccion (ej. 11B) ")

        subjets = ["español", "ingles", "sociales", "ciencias"]
        for subjet in subjets:
            while True:
                try:
                    note = float(input(f"Nota de {subjet} (0-100):"))
                    if 0 <= note <= 100:
                        student[subjet] = note
                        break
                    else: 
                        print("La nota debe estar entre 0 y 100. Intente nuevamente.")
                except ValueError:
                    print("Ingrese una nota valida (un numero). Intente nuevamente.")
        
        students.append(student)
    
    print(f"\nSe han ingresado {n} estudiantes correctamente.")

def show_students(students):
    if not students:
        print("No hay estudiantes registrados.")
        return

    print("\n--- LISTA DE ESTUDIANTES ---")
    for i, student in enumerate(students, 1):
        print(f"\nEstudiante {1}:")
        print(f"Nombre: {student['nombre']}")
        print(f"Seccion: {student['seccion']}")
        print(f"Nota de Español: {student['español']}")
        print(f"Nota de Ingles: {student['ingles']}")
        print(f"Nota de Sociales: {student['sociales']}")
        print(f"Nota de Ciencias: {student['ciencias']}")
        overall_average = (
            student["español"]
            + student["ingles"]
            + student["sociales"]
            + student["ciencias"]
        ) / 4
        print(f"Promedio General: {overall_average:.2f}")

def top3_students(students):
    if not students:
        print("No hay estudiantes registrados.")
        return

    students_with_average = []
    for student in students:
        overall_average = (
            student["español"]
            + student["ingles"]
            + student["sociales"]
            + student["ciencias"]
        ) / 4
        students_with_average.append((student, overall_average))

    students_with_average = sorted(
        students_with_average,
        key=lambda x: x[1],
        reverse=True,
    )[:3]

    print("\n--- TOP 3 ESTUDIANTES ---")
    for i, (student, average) in enumerate(students_with_average, 1):
        print(f"\nPosición {i}:")
        print(f"Nombre: , {student['nombre']}")
        print(f"Seccion: , {student['seccion']}")
        print(f"Promedio General: {average:.2f}")

def overall_average(students):
    if not students:
        print("No hay estudiantes registrados.")

    total_average = 0
    for student in students:
        total_average += (
            student["español"]
            + student["ingles"]
            + student["sociales"]
            + student["ciencias"]
        ) / 4

    average = total_average / len(students)
    print(f"\nPromedio General de todos los estudiantes: {average:.2f}")