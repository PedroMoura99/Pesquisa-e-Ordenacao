import matplotlib.pyplot as plt
from random import randint
import timeit
  
tam = [1000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
 
tempo1 = []
tempo2 = []
contaOp1 = []
contaOp2 = []
contaOp = []
 
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
    tempo = timeit.timeit("shellsort({})".format(lista), setup="from __main__ import shellsort", number = 1)
    return tempo
 
def desenhaGrafico(tempo1, tam, tempo2, contaOP1, contaOp2, xl = "N", yl = "Tempo", x2 = "N", y2 = "Operações"):
    plt.plot(tam, tempo1, label = "Complexidade: caso médio")
    plt.plot(tam, tempo2, label = "Complexidade: pior caso")
    plt.legend(bbox_to_anchor = (1, 1), bbox_transform = plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()
    plt.plot(tam, contaOp1, label = "Operações: caso médio")
    plt.plot(tam, contaOp2, label = "Operações: pior caso")
    plt.legend(bbox_to_anchor = (1, 1), bbox_transform = plt.gcf().transFigure)
    plt.ylabel(y2)
    plt.xlabel(x2)
    plt.show()
 
def shellsort(lista):
    cont = 0
    intervalo = int(len(lista) / 2)
    while (intervalo > 0):
        for i in range(intervalo, len(lista)):
            aux = lista[i]
            j = i
            while (j >= intervalo and lista[j - intervalo] > aux):
                cont += 1
                lista[j] = lista[j - intervalo]
                j -= intervalo
            lista[j] = aux
        intervalo = int(intervalo / 2)
    contaOp.append(cont)
 
for i in range(len(tam)):
    lista1 = geraLista(tam[i])
    tempo1.append(tempo(tam[i], lista1))
    lista2 = geraListaPiorCaso(tam[i])
    tempo2.append(tempo(tam[i], lista2))
 
for i in range(2 * len(tam)):
    if (i % 2 == 0):
        contaOp1.append(contaOp[i])
    else:
        contaOp2.append(contaOp[i])
 
desenhaGrafico(tempo1, tam, tempo2, contaOp1, contaOp2)
