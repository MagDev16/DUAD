import csv
import os

def export_csv(students):
    if not students:
        print("No hay estudiantes registrados para exportatar.")

    file_name = input("Ingrese el nomnre del archivo CSV (sin extension): ") + ".csv"
    with open(file_name, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=[
                "nombre",
                "seccion",
                "español",
                "ingles",
                "sociales",
                "ciencias"
            ])
            writer.writeheader()
            writer.writerows(students)

    print("Datos exportados correctamente a {file_name}")

def import_csv(students):
    file_name = input("ingrese el nombnre del archivo CSV a importar (sin extension): ") + ".csv"

    if not os.path.exists(file_name):
        print("El archivo especificado no existe.")
        return []

    students = []
    with open(file_name, mode="r', encoding='utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["español"] = float(row["español"])
            row["ingles"] = float(row["ingles"])
            row["sociales"] = float(row["sociales"])
            row["ciencias"] = float(row["ciencias"])
            students.append(row)

    print(f"Se importaron {len(students)} estudiantes desde {file_name}")
    return students