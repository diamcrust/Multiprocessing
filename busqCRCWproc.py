# practica 4: Busqueda CRCW (multiprocessing)
# Autor: Jorge de Jesús Jiménez Servín, Jose Daniel Perez Mejia, Kennet Kael Mendoza Pliego

import multiprocessing
import math
import time


def busCRCW(L, win, n):
    for i in range(n):
        win[i] = 0
    print(f'Paso 1:{win[:]}')
    time.sleep(0.5)

    for i in range(n):
        for j in range(n):
            if (L[i] > L[j]):
                win[i] = 1
    print(f'Paso 2: {win[:]}')
    time.sleep(0.5)

    for i in range(n):
        if (win[i] == 0):
            indexMin = i
    print(f'Paso 3: Indice minimo {indexMin} | Valor minimo: {L[indexMin]} (contando desde pos 0)\n ')
    


def main():
    L = multiprocessing.Array('i',[95, 10, 6, 5])
    win = multiprocessing.Array('i',[7, 7, 7, 7])
    n = len(L)

    print(f'\nNumeros: {L[:]}\n')

    t1 = multiprocessing.Process(target=busCRCW, args=(L, win, n))
    t1.start()
    t1.join()


if __name__ == "__main__":
    main()
