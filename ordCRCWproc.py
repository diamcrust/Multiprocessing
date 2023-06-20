# practica 5: Ordenamiento CRCW (procesos)
# Autor: Jorge de Jesús Jiménez Servín, Jose Daniel Perez Mejia, Kennet Kael Mendoza Pliego

import multiprocessing
import math
import time


def sortCRCR(L, win, L2, n):
    # win
    for i in range(n):
        win[i] = 0
    print(f'Paso 1: {win[:]}')
    time.sleep(0.5)

    for i in range(n):
        for j in range(n):
            if L[i] > L[j]:
                win[i] = win[i]+1
    print(f'Paso 2: {win[:]}')
    time.sleep(0.5)

    for i in range(n):
        L2[win[i]] = L[i]
    print(f'Paso 3: {L2[:]}    ------vector ordenado------\n')


def main():
    L = multiprocessing.Array('i',[95, 10, 6, 5])
    win = multiprocessing.Array('i',[9, 9, 9, 9])
    L2 = multiprocessing.Array('i',[0, 0, 0, 0])
    n = len(L)

    print(f'\nNumeros: {L[:]}\n')

    t1 = multiprocessing.Process(target=sortCRCR, args=(L, win, L2, n))
    t1.start()
    t1.join()


if __name__ == "__main__":
    main()