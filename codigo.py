import matplotlib.pyplot as plt
from random import randint
import timeit
  
def d_grafico(x, y, z, x1 = 'Quantidade de Elementos', y1 = 'Tempo'):
    plt.plot(x, y, label = "Caso Medio")
    plt.plot(x, z, label = "Pior Caso")
    plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(y1)
    plt.xlabel(x1)
    plt.show()
  
def g_lista(tam):
    lista = []
    while len(lista) != tam:
        n = randint(1, 3*tam)
        lista.append(n)
    return lista
 
def insertionSort(lis):
    for i in range(1, len(lis)):
        x = i
        y = i
        while (x > 0):
            x -= 1
            if lis[y] < lis[x]:
                aux = lis[y]
                lis[y] = lis[x]
                lis[x] = aux
                y-=1
    return lis
 
 
def g_ord(tam):
    m_lis = g_lista(tam)
    lis_ord = insertionSort(m_lis)
    return lis_ord
  
def g_ord_pior(tam):
    pior_lis = [i for i in range(tam, 0, -1)]
    lis_ord_1 = insertionSort(pior_lis)
    return lis_ord_1
  
def Tempo(q):
    tempo = timeit.timeit('g_ord({})'.format(q), setup = "from __main__ import g_ord", number = 1)
    return tempo
  
def Tempo_1(q):
    tempo = timeit.timeit('g_ord_pior({})'.format(q), setup = "from __main__ import g_ord_pior", number = 1)
    return tempo
  
x = [1000, 10000, 20000, 40000, 60000, 80000, 100000]
y = [Tempo(q) for q in x]
z = [Tempo_1(q) for q in x]
d_grafico(x, y, z)
