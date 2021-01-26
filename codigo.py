import matplotlib.pyplot as plt
from random import randint
import timeit
  
tam = [1000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
 
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
    tempo = timeit.timeit("quicksort({}, {}, {})".format(lista, 0, len(lista) - 1), setup="from __main__ import quicksort", number = 1)
    return tempo
 
def desenhaGrafico(tempo1, tam, tempo2, xl = "N", yl = "Tempo"):
    plt.plot(tam, tempo1, label = "Complexidade caso médio")
    plt.plot(tam, tempo2, label = "Complexidade pior caso")
    plt.legend(bbox_to_anchor = (1, 1), bbox_transform = plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()
 
def separa(lista, inicio, fim):
    pivo = lista[inicio]
    i = inicio + 1
    j = fim
    while (i <= j):
        if (lista[i] <= pivo):
            i += 1
        elif (pivo < lista[j]):
            j -= 1
        else:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
            j -= 1
    lista[inicio] = lista[j]
    lista[j] = pivo
    return j
 
def quicksort(lista, inicio, fim):
    while (inicio < fim):
        pivo = separa(lista, inicio, fim)
        if (pivo - inicio < fim - pivo):
            quicksort(lista, inicio, pivo - 1)
            inicio = pivo + 1
        else:
            quicksort(lista, pivo + 1, fim)
            fim = pivo - 1
 
tempo1 = []
tempo2 = []
 
for i in range(len(tam)):
    lista1 = geraLista(tam[i])
    tempo1.append(tempo(tam[i], lista1))
    lista2 = geraListaPiorCaso(tam[i])
    tempo2.append(tempo(tam[i], lista2))
 
desenhaGrafico(tempo1, tam, tempo2)
