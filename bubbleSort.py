import matplotlib.pyplot as plt
import random
import timeit


def drawGraphic(x, y, xl="Entradas", yl="Saídas"):
    plt.plot(x, y)
    plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()


def generateRandomList(tam):
    random_list = []
    while len(random_list) != tam:
        n = random.randint(1, tam)
        random_list.append(n)
    return random_list


def compareTime(quantity):
    print('calculando para ' + str(quantity))
    time = timeit.timeit("generateAndOrder({})".format(quantity), setup="from __main__ import generateAndOrder",
                         number=1)
    print('tempo necessário: ' + str(time))
    return time


def bubbleSort(array):
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux
    return array


def generateAndOrder(tam):
    ## list_to_sort = [i for i in range(tam, 0, -1)]
    # Leave the live above to worst case

    ## list_to_sort = generateRandomList(tam)
    # Leave the line above to medium case

    ordered_list = bubbleSort(list_to_sort)


numbers_to_generate = [1000, 10000, 20000, 30000, 40000, 50000]
time_to_generate = [compareTime(quantity) for quantity in numbers_to_generate]

drawGraphic(numbers_to_generate, time_to_generate, "Números Gerados", "Tempo")