# practica 1: Suma EREW (procesos)
# Autor: Jorge de Jesús Jiménez Servín, Jose Daniel Perez Mejia, Kennet Kael Mendoza Pliego


import multiprocessing
import math
import time



def suma(i, j, A):
    if (((2*j) % (math.pow(2, i))) == 0):
        A[(2*j)] = A[(2*j)]+A[int((2*j)-(math.pow(2, i-1)))]
    time.sleep(0.5)

def main():
    A = multiprocessing.Array('i', [0, 1, 1, 1, 1, 1, 1, 1, 1])  # Vector compartido
    n = len(A)-1
    log = (int)(math.log(n, 2))
    processes = []

    print(f"\nElementos del vector A {A[:]}")
    print(f'Numero de elementos: {n}\n')
    print(f'{A[1:n+1]}\n')

    for i in range(1, log+1):
        print(f'Paso: {i}')
        for j in range(1, (int)(n/2)+1):
            p1 = multiprocessing.Process(target=suma, args=(i, j, A))
            processes.append(p1)
            p1.start()

        for p in processes:
            p.join()

        print(f'{A[1:n+1]}\n')

    print(f'Suma= {A[n]}')

if __name__ == "__main__":
    main()