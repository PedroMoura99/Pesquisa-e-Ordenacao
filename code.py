import matplotlib.pyplot as plt
from random import randint
import timeit
   
tam = [1000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
  
tempo1 = []
tempo2 = []
  
def geraLista(tam):
    lista = []
    while (len(lista) < tam):
        n = randint(1, 5*tam)
        if n not in lista:
            lista.append(n)
    return lista
   
def geraListaPiorCaso(tam):
    lista = []
    j = tam
    while (j > 0):
        lista.append(j)
        j = j - 1
    return lista
   
def tempo(tamanho, lista):
    tempo = timeit.timeit("heapsort({})".format(lista), setup="from __main__ import heapsort", number = 1)
    return tempo
  
def desenhaGrafico(tempo1, tam, tempo2, xl = "N", yl = "Tempo", x2 = "N", y2 = "Operações"):
    plt.plot(tam, tempo1, label = "Complexidade: caso médio")
    plt.plot(tam, tempo2, label = "Complexidade: pior caso")
    plt.legend(bbox_to_anchor = (1, 1), bbox_transform = plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()
 
def heapsort(lista):
    #print(lista)
    n = len(lista)
    i = len(lista) // 2
    while (True):
        if (i > 0):
            i -= 1
            t = lista[i]
        else:
            n -= 1
            if (n == 0):
                return
            t = lista[n]
            lista[n] = lista[0]
        pai = i
        filho = (i * 2) + 1
        while (filho < n):
            if ((filho + 1 < n) and (lista[filho + 1] > lista[filho])):
                filho += 1
            if (lista[filho] > t):
                lista[pai] = lista[filho]
                pai = filho
                filho = (pai * 2) + 1
            else:
                break
        lista[pai] = t
 
 
for i in range(len(tam)):
    lista1 = geraLista(tam[i])
    tempo1.append(tempo(tam[i], lista1))
    lista2 = geraListaPiorCaso(tam[i])
    tempo2.append(tempo(tam[i], lista2))
 
desenhaGrafico(tempo1, tam, tempo2)
