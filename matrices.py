def mostrar_matriz_por_columna(m1):
    for c in range(5):
        for f in range(4):
            print(m1[f][c])


def crear_matriz():
    m1 = []
    n = 4
    m = 5
    for i in range(n):
        m1.append([])
        for c in range(m):
            m1[i].append(i+1)
    mostrar_matriz_por_columna(m1)
    return m1


def mostrar_matriz_por_fila(m1):
    cont = 0
    for f in range(len(m1)):
        for c in range(len(m1[f])):
            print(m1[f][c])

def crear_matrizII():
    n = 5
    m2 = [None] * n
    for i in range(n):
        m2[i] = [0] * 4
    print(m2)


def crear_matrizIII():
    filas, columnas  = 2, 2
    m3 = [[None] * columnas for f in range(filas)]
    for f in range(columnas):
        for c in range(filas):
            m3[f][c] = int(input('Valor númerico: '))
    print(m3, sep='\n')

crear_matrizIII()
#crear_matrizII()
