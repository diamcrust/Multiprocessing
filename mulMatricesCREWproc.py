# practica 7: Multiplicación Matrices CREW (procesos)
# Autor: Jorge de Jesús Jiménez Servín, Jose Daniel Perez Mejia, Kennet Kael Mendoza Pliego


from multiprocessing import Process, Value, Lock
import math
import time

def proc1(i, j, k, A, B, C, lock):
    with lock:
        C[k][i][j].value = int(A[i][k].value) * int(B[k][j].value)
    time.sleep(0.1)

def proc2(i, j, k, l, C, C2, lock):
    with lock:
        if (((2 * k) % (2 ** l)) == 0):
            C2[2 * k][i][j].value = int(C[2 * k][i][j].value + C[2 * k - (2 ** l)][i][j].value)
    time.sleep(0.2)


def main():
    lock = Lock()
    A = [[Value('i', 0) for _ in range(2)] for _ in range(2)] # value
    B = [[Value('i', 0) for _ in range(2)] for _ in range(2)]
    C = [[[Value('i', 0) for _ in range(2)] for _ in range(2)] for _ in range(2)]
    C2 = [[[Value('i', 0) for _ in range(2)] for _ in range(2)] for _ in range(2)]
    
    lg = int(math.log(2, 2))
    print ("\nFunciona INSERTANDO MATRIZ 2X2 DESEADA\n\nEstablecer matriz A:")
    i = 0
    while i < 2:
        j = 0
        while j < 2:
            print ("Valor componente [", i + 1, ", ", j + 1, " ]: ")
            x = int(input())
            A[i][j].value = x
            j += 1
        i += 1

    print ("\nEstablecer matriz B:")
    i = 0
    while i < 2:
        j = 0
        while j < 2:
            print ("Valor componente [", i + 1, ",", j + 1, "]")
            x = int(input())
            B[i][j].value = x
            j += 1
        i += 1


    print ("\nProcedimiento de multiplicación de matrices: \n")
    print ("[ ", A[0][0].value, " ", A[0][1].value, " ]  X  [ ", B[0][0].value, "  ", B[0][1].value, " ]")
    print ("[ ", A[1][0].value, " ", A[1][1].value, " ]  X  [ ", B[1][0].value, "  ", B[1][1].value, " ]")

    k = 0
    while k < 2:
        i=0
        while(i<2):
            j=0
            while(j<2):
                t1=Process(target=proc1,args=(i,j,k,A,B,C,lock))
                t1.start()
                t1.join()
                j=j+1
            i=i+1
        k=k+1


    print ("\n\nPrimer paso: \n[",C[0][0][0].value, ',',C[0][0][1].value,']')
    print ('[',C[0][1][0].value,',',C[0][1][1].value,']')
    print ('[',C[1][0][0].value, ',',C[1][0][1].value,']')
    print ('[',C[1][1][0].value, ',',C[1][1][1].value,']')

    l=0
    while(l<lg):
        i=0
        while(i<2):
            j=0
            while(j<2):
                k=0
                while(k<1):
                    t2=Process(target=proc2,args=(i,j,k,l,C,C2,lock))
                    t2.start()
                    t2.join()
                    k=k+1
                j=j+1
            i=i+1
        l=l+1


    print ("\nSegundo paso: [A]*[B] = \n")

    print ("[ ", C2[0][0][0].value, "  ", C2[0][0][1].value, " ]") # se accede a lo valores con value
    print ("[ ", C2[0][1][0].value, "  ", C2[0][1][1].value, " ]")

if __name__ == "__main__":
    main()