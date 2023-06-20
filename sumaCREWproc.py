# practica 2: Suma CREW   (procesos)                           FINAL
# Autor: Jorge de Jesús Jiménez Servín, Jose Daniel Perez Mejia, Kennet Kael Mendoza Pliego

import multiprocessing
from multiprocessing import Barrier, Lock, Process
import math
import time


def suma(i, j, A, lock, n, barrier):
    a = A[j]
    b = A[j-(int)(math.pow(2, i-1))]

    barrier.wait()
    with lock:
        A[j] = a+b
    time.sleep(0.5)


def main():
    lock = Lock()
    A = multiprocessing.Array('i',[0, 1, 1, 1, 1, 1, 1, 1, 1]) #vector compartido
    n = len(A)
    log = (int)(math.log(n, 2))
    j = 1
    processes = []

    print(f"\nElementos del vector A {A[:]}")
    print(f'Numero de elementos: {n-1}\n')
    print(f'{A[1:n+1]}\n')
    for i in range(1, log+1):
        print(f'Paso: {i}')
        barrier = Barrier(n-(int)(math.pow(2, i-1)+1))
        for j in range((int)(math.pow(2, i-1)+1), n):
            t1 = Process(target=suma, args=(i, j, A, lock, n, barrier))
            processes.append(t1)
            t1.start()

        for hilo in processes:
            hilo.join()
        print(f'{A[1:n+1]}\n')

    print(f'Suma= {A[n-1]}')


if __name__ == "__main__":
    main()
