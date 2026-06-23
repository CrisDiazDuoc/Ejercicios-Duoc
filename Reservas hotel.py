import random

habitaciones = {}

def generar_codigo(tipo):
    prefijo = tipo[:2].upper()
    while True:
        numero_aleatorio = random.randint(100, 999)
        codigo = prefijo + str(numero_aleatorio)
        if codigo not in habitaciones:
            return codigo
        
def solicitar_numero_habitacion():
    while True:
        try:
            numero = int(input("Ingrese el número de habitación: "))
            return numero
        except:
            print("Debe ingresar un valor numérico entero.")

def solicitar_tipo_habitacion():
    while True:
        tipo = input("Ingrese el tipo de habitación (Simple/Doble/Suite): ").capitalize()
        if tipo == "Simple" or tipo == "Doble" or tipo == "Suite":
            return tipo
        else:
            print("Tipo no válido. Por favor ingrese Simple, Doble o Suite.")

def registrar_habitacion():
    print("\n<-> Registrar Habitación <->")
    numero = solicitar_numero_habitacion()
    tipo = solicitar_tipo_habitacion()
    
    codigo = generar_codigo(tipo)
    
    habitaciones[codigo] = {
        "codigo": codigo,
        "numero": numero,
        "tipo": tipo,
        "estado": "Disponible"
    }
    print(f"Habitación registrada correctamente. Código asignado: {codigo}")

def mostrar_habitaciones():
    print("\n<-> Listado Habitaciones <->")
    if len(habitaciones) == 0:
        print("No hay habitaciones registradas en el sistema.")
    else:
        for cod, datos in habitaciones.items():
            print(f"Código: {datos['codigo']} | Número: {datos['numero']} | Tipo: {datos['tipo']} | Estado: {datos['estado']}")

def buscar_habitacion():
    print("\n<-> Buscar Habitación <->")
    codigo = input("Ingrese el código de la habitación a buscar: ").upper()
    
    if codigo in habitaciones:
        datos = habitaciones[codigo]
        print(f"\nInformación de la habitación:\n- Código: {datos['codigo']}\n- Número: {datos['numero']}\n- Tipo: {datos['tipo']}\n- Estado: {datos['estado']}")
    else:
        print(f"La habitación con el código '{codigo}' no existe.")

def reservar_habitacion():
    print("\n<-> Reservar Habitación <->")
    codigo = input("Ingrese el código de la habitación a reservar: ").upper()
    
    if codigo in habitaciones:
        if habitaciones[codigo]["estado"] == "Disponible":
            habitaciones[codigo]["estado"] = "Ocupada"
            print(f"La habitación {codigo} ha sido reservada.")
        else:
            print(f"La habitación {codigo} ya se encuentra ocupada.")
    else:
        print(f"La habitación con el código '{codigo}' no existe.")

def liberar_habitacion():
    print("\n<-> Liberar Habitación <->")
    codigo = input("Ingrese el código de la habitación a liberar: ").upper()
    
    if codigo in habitaciones:
        if habitaciones[codigo]["estado"] == "Ocupada":
            habitaciones[codigo]["estado"] = "Disponible"
            print(f"La habitación {codigo} ha sido liberada.")
        else:
            print(f"La habitación {codigo} ya se encuentra Disponible.")
    else:
        print(f"La habitación con el código '{codigo}' no existe.")

def modificar_habitacion():
    print("\n<-> Modificar Habitación <->")
    codigo = input("Ingrese el código de la habitación a modificar: ").upper()
    
    if codigo in habitaciones:
        print("Ingrese los nuevos datos (el código y estado no se modificarán):")
        nuevo_numero = solicitar_numero_habitacion()
        nuevo_tipo = solicitar_tipo_habitacion()
        
        habitaciones[codigo]["numero"] = nuevo_numero
        habitaciones[codigo]["tipo"] = nuevo_tipo
        
        print(f"La habitación {codigo} ha sido modificada correctamente.")
    else:
        print(f"La habitación con el código '{codigo}' no existe.")

def eliminar_habitacion():
    print("\n<-> Eliminar Habitación <->")
    codigo = input("Ingrese el código de la habitación a eliminar: ").upper()
    
    if codigo in habitaciones:
        del habitaciones[codigo]
        print(f"La habitación {codigo} ha sido eliminada del sistema.")
    else:
        print(f"La habitación con el código '{codigo}' no existe.")

def mostrar_menu():
    print("\n === Sistema Reservas de Hotel ===\n1. Registrar habitación\n2. Mostrar habitaciones\n3. Buscar habitación\n4. Reservar habitación\n5. Liberar habitación\n6. Modificar habitación\n7. Eliminar habitación\n8. Salir")

def principal():
    opcion = 0
    while opcion != 8:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción (1-8): ")) 
            if opcion == 1:
                registrar_habitacion()
            elif opcion == 2:
                mostrar_habitaciones()
            elif opcion == 3:
                buscar_habitacion()
            elif opcion == 4:
                reservar_habitacion()
            elif opcion == 5:
                liberar_habitacion()
            elif opcion == 6:
                modificar_habitacion()
            elif opcion == 7:
                eliminar_habitacion()
            elif opcion == 8:
                print("Saliendo del sistema.")
            else:
                print("Opción inválida.")
        except:
            print("Debe ingresar un número.")

principal()