# practica 6.2: Ordenamiento EREW oddEvenMerge (procesos)
# Autor: Jorge de Jesús Jiménez Servín, Jose Daniel Perez Mejia, Kennet Kael Mendoza Pliego

import multiprocessing


def proc1(L, i, odd, even):
    L[2 * i] = odd[i]
    L[2 * i + 1] = even[i]


def proc2(L, i):
    if L[2 * i + 1] < L[2 * i]:
        L[2 * i + 1], L[2 * i] = L[2 * i], L[2 * i + 1]


def oddEvenSplit(L):
    n = len(L)
    aux = int(n / 2)
    L1 = L[0:aux]
    L2 = L[aux:n]
    return L1, L2


def oddEvenMergePRAM(L):
    n = len(L)
    if n == 2:
        if L[0] > L[1]:
            L[0], L[1] = L[1], L[0]
    else:
        odd, even = oddEvenSplit(L)
        oddEvenMergePRAM(odd)
        oddEvenMergePRAM(even)

        return odd, even


def main():
    L = multiprocessing.Array(
        'i', [16, 22, 35, 40, 55, 66, 70, 85, 15, 18, 23, 53, 60, 69, 72, 78])
    print(f'\nNumeros: {L[:]}\n')

    odd, even = oddEvenMergePRAM(L)

    processes = []
    for i in range(0, int(len(L) / 2)):
        p1 = multiprocessing.Process(target=proc1, args=(L, i, even, odd))
        p1.start()
        processes.append(p1)

    for p in processes:
        p.join()

    processes = []
    for i in range(0, int(len(L) / 2)):
        p2 = multiprocessing.Process(target=proc2, args=(L, i))
        p2.start()
        processes.append(p2)

    for p in processes:
        p.join()

    print(oddEvenMergePRAM(even))
    print(oddEvenMergePRAM(odd))
    print(oddEvenSplit(L))
    print(oddEvenMergePRAM(L))
    print('\n Numeros ordenados: \n', L[:], '\n')


if __name__ == '__main__':
    main()
