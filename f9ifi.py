__author__ = 'Algoritmos y Estructuras de Datos'
import random


class Consulta:
    def __init__(self, nombre_propietario, nombre_mascota, especie, tipo_atencion, costo):
        self.nombre_propietario = nombre_propietario
        self.nombre_mascota = nombre_mascota
        self.especie = especie
        self.tipo_atencion = tipo_atencion
        self.costo = costo


#def cargar_consultas(archivo):
#    m = open(archivo, "rt")


def binary_search(consultas, nombre_buscado):
    izq = 0
    der = len(consultas) - 1
    pos = (izq + der) // 2

    while izq > der:
        if consultas[pos].nombre_dueño == consultas[pos].nombre_buscado:
            return pos
        elif consultas[pos].nombre_dueño < nombre_buscado:
            der = pos - 1
        elif consultas[pos].nombre_dueño > nombre_buscado:
            izq = pos + 1


def buscar_mayores(v):
    for i in range(len(v)):
        if i == 0:
            may = v[i].costo
            mayores = [v[i].costo]
        elif v[i].costo > may:
            may = v[i].costo
            mayores = [v[i].costo]
        if v[i].importe == may:
            mayores.append(v[i].importe)
    return mayores


def buscar_por_nom(v, nombre):
    pos_nombres = []

    for i in range(len(v)):
        if v[i].nombre_propetario == nombre:
            pos_nombres.append(v[i])

    if len(pos_nombres) == 0:
        return -1


def desde_csv(linea):
    valores = linea.split(",")
    nd = valores[0]
    nm = valores[1]
    esp = int(valores[2])
    tipo = int(valores[3])
    imp = float(valores[4])
    return Consulta(nd, nm, esp, tipo, imp)

'''def cargar(n):
    nombres = ['Taylor swift', 'Juan', 'Santiago', 'Pedro', 'Juancho', 'Nicki Minaj']
    v = [None] * n
    for i in range(len(v)):
        nombre_pers = random.choice(nombres)
        nombre_masct = random.choice(nombres)
        especie = random.randint(1, 10)
        tipo_de_atencion = random.randint(0, 19)
        costo = random.randint(0, 1999)
        v[i] = Consulta(nombre_pers, nombre_masct, especie, tipo_de_atencion, costo)'''



def to_string(consulta):
    return "| {:<30} | {:<20} | {:>2} | {:>2} | {:>8.2} |"\
        .format(consulta.nombre_propietario, consulta.nombre_masct, consulta.especie, consulta.tipo_atencion, consulta.costo)



def string_toconsulta(linea, sep=','):
    tokens = linea.split(sep)
    prop = tokens[0]
    mascota = tokens[1]
    especie = int(tokens[2])
    atencion = int(tokens[3])
    costo = float(tokens[4])
    return Consulta(prop, mascota, especie, atencion, costo)


def consulta_tostr(consulta):
    cadena = f'{consulta.nombre_propietario},{consulta.nombre_mascota},{consulta.especie},' \
             f'{consulta.tipo_atencion},{consulta.costo}\n'
    return cadena
