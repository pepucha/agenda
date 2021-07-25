'''Ejercicio 2 - Agenda

Utilizando los conceptos de Listas, Tuplas y Diccionarios, desarrollar una agenda.
Cada entrada en la agenda debe contener los datos de contacto de una persona:
    * DNI
    * Nombre
    * Apellido
    * email
    * Teléfonos (como máximo 2)
    
La agenda debe permitir agregar, modificar y eliminar contactos.

Desarrollar un menú que permita al usuario utilizar la agenda. El menú debe poseer las siguientes opciones:
    1 - Agregar un contacto
    2 - Modificar un contacto existente.
    3 - Eliminar un contacto existente.
    4 - Salir.
    
Para las opciones 2 y 3, se debe ingresar el DNI del contacto en cuestión.

La opción de modificar un contacto, debe permitir modificar todos los campos excepto el DNI.
'''
#import pathlib

agenda = dict()
respuesta_menu = 0
#contactos = ''
AGREGAR = 1
MODIFICAR = 2
ELIMINAR = 3
SALIR = 4

'''
if pathlib.Path(contactos).exists():
    with open(contactos, 'r') as contactos:
        for linea in contactos:
            dni, nombre, apellido, telefono, email = linea.strip().split(',')
            agenda.setdefault(dni,[nombre, apellido, telefono, email])
else:  '''  
with open('contactos.txt', 'r') as contactos:
    pass 

while respuesta_menu != 4:

    respuesta_menu = int(input("""
    Marque un numero dependiendo de la accion a realizar:
    1 - Agregar un contacto.
    2 - Modificar un contacto existente.
    3 - Eliminar un contacto existente.
    4 - Salir.
    Respuesta: """))

    if respuesta_menu == AGREGAR:
        print("\nIngresa los datos para agregar un nuevo contacto.")
        dni = input("DNI: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        telefono = int(input("Telefono: "))
        email = input("Email: ")
        agenda.setdefault(dni,[nombre, apellido, telefono, email]) #Se agregan los datos ingresados al diccionario.
        with open('contactos.txt', 'a') as contactos: #Se abre el archivo modo append
            contactos.write(f'{dni}, {nombre}, {apellido}, {telefono},{email}\n') #Se introducen los datos del contacto al archivo.
        #agenda[dni] = { 
           # 'nombre' : nombre,
           # 'apellido' : apellido ,
           # 'telefono' : telefono,
           # 'email' : email 
           # }  Otra manera de ingresar los datos al diccionario.
            print("------------Contacto agendado---------------")
            
    elif respuesta_menu == MODIFICAR:
        if len(agenda) > 0: #Este if valida si la agenda tiene contactos para poder modificar.
            dni = input("\nIngresa el DNI del contacto que se desea modificar: \n")
            if dni in agenda:
                print("\nIngresa los datos para modificar un contacto existente.")
                nuevo_nombre = input("Ingresa el nuevo nombre: \n")
                nuevo_apellido = input("Ingresa el nuevo apellido: \n")
                nuevo_telefono = int(input("Ingresa el nuevo telefono: \n"))
                agenda[dni] = nuevo_nombre, nuevo_apellido, nuevo_telefono, email
                print("------------Contacto modificado---------------")
            else:
                print("El contacto no esta registrado.")
        else: 
            print("La agenda no tiene contactos")

    elif respuesta_menu == ELIMINAR:
        if len(agenda) > 0: #Este if valida si la agenda tiene contactos para poder eliminar.
            dni = input("\nIngresa el DNI del contacto que desea eliminar: \n")

            if dni in agenda:
                agenda.pop(dni)
                print("------------Contacto eliminado---------------")
                
            else:
                print("El contacto no esta registrado.")
        else:
            print("La agenda no tiene contactos agregados.")   

print("Saliste de la app.")
        