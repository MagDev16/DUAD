from actions import (
    add_students,
    show_students,
    top3_students,
    overall_average
)

from data import export_csv, import_csv

def show_main_menu(students):
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ingresar información de estudiantes")
        print("2. Ver información de todos los estudiantes")
        print("3. Ver top 3 estudiantes con mejor promedio")
        print("4. Ver nota promedio general")
        print("5. Exportar datos a CSV")
        print("6. Importar datos desde CSV")
        print("7. Salir")

        option = input("Selecciones una opción (1-7): ")

        if option  == "1":
            add_students(students)
        elif option == "2":
            show_students(students)
        elif option == "3":
            top3_students(students)
        elif option == "4":
            overall_average(students)
        elif option == "5":
            export_csv(students)
        elif option == "6":
            students.extend(import_csv(students))
        elif option == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida (1-7).")