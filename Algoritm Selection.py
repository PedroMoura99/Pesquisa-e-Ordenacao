import random
from timeit import timeit
import matplotlib.pyplot as plt

tam = [1000,10000,20000,40000,80000,100000]

def selectionSort(list):
    for i in range(len(list)):
        menor = i
        for j in range(i+1,len(list)):
            if((list[j] < list[menor])):
                menor = j
        list[i], list[menor] = list[menor],list[i]
    return list

def geraLista(tam):
    Lista = []
    while(len(Lista)<tam):
        n = random.randint(1,1*tam)
        Lista.append(n)
    return Lista

def geraListaDecrescente(tam):
    Lista = []
    while (tam>0):
        Lista.append(tam)
        tam-=1
    return Lista

def time():
    temp = []
    for i in range(len(tam)):
        temp.append(timeit("selectionSort({})".format(geraLista(tam[i])), setup="from __main__ import selectionSort", number=1))
    return temp

def Pior():
    temp = []
    for i in range(len(tam)):
        temp.append(timeit("selectionSort({})".format(geraListaDecrescente(tam[i])), setup="from __main__ import selectionSort", number=1))
    return temp


def desenhaGrafico(time,time2, tam):
    plt.title("Selection Sort: Tempo Médio x Pior Tempo")
    plt.plot(time, tam, label="Tempo Médio", color = 'blue')
    plt.plot(time2, tam, label="Pior Tempo", color='red')
    plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    xl = "Tempo(s)"
    yl = "Tamanho"
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()

desenhaGrafico(time(),Pior(),tam)
