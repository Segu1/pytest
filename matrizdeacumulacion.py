'''6. Veterinaria

Una veterinaria nos solicito un programa que nos permita obtener
estadísticas de sus consultas para mascotas, de cada consulta se tiene un nombre del propietario, nombre de la mascota,
 especie de la mascota (un valor entre 1 y 10), tipo de atención (un valor entre 0 y 19) y el costo de la consulta.
 En base a esto y a partir del archivo mascotas.csv, cargar un arreglo ordenado por nombre de propietario y mediante un
 menú de opciones realizar las siguientes operaciones:

1 - Buscar y mostrar la consulta con el mayor costo, si existe mas
de una consulta con un costo igual al mayor mostrar todas.

2 - Buscar las consultas hechas por un propietario cuyo nombre
es igual a nom (ingresado por teclado), mostrar todos las consultas hechas por ese propietario a partir de la primera
que encuentre.

3 - Obtener el total por especie de mascota y tipo de atención, 200 acumuladores) en una matriz de conteo.
 Muestre valores distintos a cero

4 - Generar un archivo binario especie.dat con todas las consultas hechas a mascotas que no sean de a especia 3 o 7.
 Mostrar dicho archivo'''

import f9ifi
#descargar cascadia code
__author__ = 'Algoritmos y Estructuras de Datos'
import f9ifi
import os

def menu():
    cadena = 'Menu de Opciones\n' \
             '========================================\n' \
             '1 --- Buscar y mostrar la consulta con el mayor costo\n' \
             '2 ... Buscar las consultas hechas por un propietario\n' \
             '3 --- Obtener el total por especie de mascota y tipo de atención\n ' \
             '4 --- Generar un archivo binario especie.dat con todas las consultas hechas a mascotas\n' \
             '0 --- Salir\n' \
             'Ingrese su opcion: '
    return int(input(cadena))


def cargar_consultas(archivo, consultas):
    if not os.path.exists(archivo):
        return None

    m = open(archivo, "rt")
    while True:
        linea = m.readline()
        if linea == "":
            break
        registros = f9ifi.desde_csv(linea)
        consultas.append(registros)


def add_in_order(vector, consulta):
    izq = 0
    der = len(vector)

    while izq <= der:
        pos = (izq + der) / 2
        if vector[pos].nombre_dueño == consulta.nombre_dueño:
            break
        elif vector[pos].nombre_dueño < consulta.nombre_dueño:
            izq = pos + 1
        else:
            der = pos - 1

        if izq > der:
            pos = izq

        vector[pos:pos] = [consulta]


def principal():
    opcion = -1
    consultas = []
    consulta = cargar_consultas('mascotas.csv', consultas)


    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            for i in range(len(consultas)):
                f9ifi.to_string(consultas[i])
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass


if __name__ == '__main__':
    principal()
