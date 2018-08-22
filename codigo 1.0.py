from threading import Thread
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
    tempo = timeit.timeit("mergesort({}, {}, {})".format(lista, 0, len(lista) - 1), setup="from __main__ import mergesort", number = 1)
    return tempo
  
def desenhaGrafico(tempo1, tam, tempo2, xl = "N", yl = "Tempo"):
    plt.plot(tam, tempo1, label = "Complexidade caso médio")
    plt.plot(tam, tempo2, label = "Complexidade pior caso")
    plt.legend(bbox_to_anchor = (1, 1), bbox_transform = plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()
     
def intercala(lista, esquerda, meio, direita):
    tam1 = meio - esquerda + 1
    tam2 = direita - meio
 
    listaEsquerda = [0] * tam1
    listaDireita = [0] * tam2
 
    for i in range(tam1):
        listaEsquerda[i] = lista[esquerda + i]
    for j in range(tam2):
        listaDireita[j] = lista[meio + 1 + j]
 
    i = 0
    j = 0
    k = esquerda
 
    while (i < tam1 and j < tam2):
        if (listaEsquerda[i] <= listaDireita[j]):
            lista[k] = listaEsquerda[i]
            i += 1
        else:
            lista[k] = listaDireita[j]
            j += 1
        k += 1
 
    while (i < tam1):
        lista[k] = listaEsquerda[i]
        i += 1
        k += 1
 
    while (j < tam2):
        lista[k] = listaDireita[j]
        j += 1
        k += 1
 
 
def mergesort(lista, esquerda, direita):
    if (esquerda < direita):
        meio = int((esquerda + (direita - 1)) / 2)
        mergesort(lista, esquerda, meio)
        mergesort(lista, meio + 1, direita)
        intercala(lista, esquerda, meio, direita)
     
tempo1 = []
tempo2 = []
 
for i in range(len(tam)):
    lista1 = geraLista(tam[i])
    tempo1.append(tempo(tam[i], lista1))
    lista2 = geraListaPiorCaso(tam[i])
    tempo2.append(tempo(tam[i], lista2))
 
desenhaGrafico(tempo1, tam, tempo2)
