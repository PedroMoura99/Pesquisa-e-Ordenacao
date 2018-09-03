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
    tempo = timeit.timeit("countingsort({})".format(lista), setup="from __main__ import countingsort", number = 1)
    return tempo
 
def desenhaGrafico(tempo1, tam, tempo2, xl = "N", yl = "Tempo", x2 = "N", y2 = "Operações"):
    plt.plot(tam, tempo1, label = "Complexidade: caso médio")
    plt.plot(tam, tempo2, label = "Complexidade: pior caso")
    plt.legend(bbox_to_anchor = (1, 1), bbox_transform = plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()
 
def countingsort(lista):
    contador = [0] * (max(lista) + 1)
    resultado = [0] * len(lista)
    for i in range (len(lista)):
        contador[lista[i]] += 1
    for i in range(min(lista), len(contador)):
        contador[i] = contador[i] + contador[i - 1]
    for i in range(len(lista)):
        resultado[contador[lista[i]] - 1] = lista[i]
        contador[lista[i]] -= 1
    return resultado
 
for i in range(len(tam)):
    lista1 = geraLista(tam[i])
    tempo1.append(tempo(tam[i], lista1))
    lista2 = geraListaPiorCaso(tam[i])
    tempo2.append(tempo(tam[i], lista2))
 
desenhaGrafico(tempo1, tam, tempo2)
