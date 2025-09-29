# tarea_diccionarios.py
# Autor: Reemplaza con tu nombre
# Fecha: 28/09/2025
# Descripción: Ejercicio sobre diccionarios en Python. Se siguen las instrucciones
#              de la tarea: crear, modificar, verificar, eliminar y mostrar el diccionario.
#
# Comentarios: Este código está escrito con explicaciones sencillas, como lo haría
#              un estudiante de bachillerato. Puedes ejecutar el archivo con:
#              python3 tarea_diccionarios.py

def main():
    # 1. Crear diccionario con información personal (valores ficticios)
    informacion_personal = {
        "nombre": "María López",     # nombre de la persona (ficticio)
        "edad": 17,                  # edad (se eliminará más adelante)
        "ciudad": "Cuenca",          # ciudad inicial
        "profesion": "Estudiante"    # profesión inicial
    }

    # 2. Acceder y modificar el valor de "ciudad"
    # Primero mostramos la ciudad que tenía y luego la cambiamos por otra.
    print("Ciudad original:", informacion_personal["ciudad"])
    informacion_personal["ciudad"] = "Guayaquil"  # actualizamos la ciudad

    # 3. Agregar o actualizar la clave "profesion"
    # Si la clave ya existe la actualizamos; si no existe la añadimos.
    informacion_personal["profesion"] = "Técnico en Informática"

    # 4. Verificar si la clave "telefono" existe; si no, agregarla
    # Usamos un número ficticio para no usar datos reales.
    if "telefono" not in informacion_personal:
        informacion_personal["telefono"] = "+593987654321"

    # 5. Eliminar la clave "edad" porque la tarea pide quitarla
    # Usamos pop con valor por defecto para evitar errores si no existe.
    informacion_personal.pop("edad", None)

    # 6. Imprimir el diccionario final de forma clara
    print("\nDiccionario final:")
    for clave, valor in informacion_personal.items():
        print(f"  {clave}: {valor}")

if __name__ == "__main__":
    main()
