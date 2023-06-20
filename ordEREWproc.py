# practica 6: Ordenamiento EREW   MergeSort FINAL (procesos)
# Autor: Jorge de Jesús Jiménez Servín, Jose Daniel Perez Mejia, Kennet Kael Mendoza Pliego

import multiprocessing
import math
from time import sleep

def mergeSort(N):
    
    print(f"Split {N[:]}")
    if len(N) > 1:

        helf = len(N)//2
        lefthelf = N[:helf]
        righthelf = N[helf:]
        

        mergeSort(lefthelf)
        mergeSort(righthelf)

        i=0
        j=0
        k=0

        while i < len(lefthelf) and j < len(righthelf):

            if lefthelf[i] < righthelf[j]:

                N[k] = lefthelf[i]
                i += 1

            else:

                N[k] = righthelf[j]
                j += 1

            k += 1

        while i < len(lefthelf):

            N[k] = lefthelf[i]
            i += 1
            k += 1

        while j < len(righthelf):

            N[k] = righthelf[j]
            j += 1
            k += 1
    print(f"Merge {N[:]}")
    sleep(0.2)
    
    
    

def main():
    N = multiprocessing.Array('i',[16, 22, 35, 40, 53, 66, 70, 85, 15, 18, 23, 55, 60, 69, 72, 78])

    print(f'\nNumeros: {N[:]}\n')

    t1 = multiprocessing.Process(target=mergeSort, args=(N,))
    t1.start()
    t1.join()

    print(f'\nNumeros ordenados: {N[:]}\n')
    
if __name__ == "__main__":
    main()