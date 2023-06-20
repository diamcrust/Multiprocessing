# practica 3: Busqueda EREW (procesos)
# Autor: Jorge de Jesús Jiménez Servín, Jose Daniel Perez Mejia, Kennet Kael Mendoza Pliego

import multiprocessing
import math
import time


def broadcast(x, i, temp):
    j = 0
    while (j < (int)(math.pow(2, i-1))):
        if (j <= (int)(math.pow(2, i-1)+1)):
            temp[j] = x
        j = j+1
    time.sleep(0.3)

def searchmin(i, L, temp):
    if (L[i] == temp[i]):
        temp[i] = i
    else:
        temp[i] = 0
    time.sleep(0.3)

def min(n, temp):
    for i in range(n):
        if (temp[i] == 0):
            temp[i] = temp[i+1]
            temp[i+1] = 0
        else:
            if (temp[i] < temp[i+1]):
                temp[i+1] = 0
    time.sleep(0.3)

def main():
    L = multiprocessing.Array('i',[-2, -1, 23, -4, 2, 5, -2, 0, 5, 1, 5, -5, 8, 5, 3, -2])
    temp = multiprocessing.Array('i',[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    x = 3
    n = len(L)-1
    log = (int)(math.log(n)/math.log(2)+3)

    print(f"\nElementos del vector A {L[:]}")
    print(f'Numero de elementos: {n+1}')
    print(f'Buscando a {x}...\n')
    

    print("BROADCAST = DIFUSION")
    for i in range(1, log):
        t1 = multiprocessing.Process(target=broadcast, args=(x, i, temp))
        t1.start()
        t1.join()
        print(temp[:])

    print("\nSEARCH EREW = COMPARACIÓN")
    for i in range(n+1):
        t2 = multiprocessing.Process(target=searchmin, args=(i, L, temp))
        t2.start()
        t2.join()
        print(temp[:])

    print("\nSEARCH MIN = ELEMENTO MINIMO")
    for j in range(1, n+1):
        t3 = multiprocessing.Process(target=min, args=(n, temp))
        t3.start()
        t3.join()
        print(temp[:])
    print('\nFuncion min:', temp[:])
    print(f'\nNumero ({x}) en la pos', temp[0],'(considerando pos inicial = 0)\n')


if __name__ == "__main__":
    main()
