from queue import PriorityQueue
import os
import time

y = 0
x = 0


def read_file(filename):
    global x, y
    lines = None
    start = (0, 0)
    end = (0, 0)

    with open(filename) as file:
        lines = file.readlines()

        j = 0
        for line in lines:
            lines[j] = line.strip('\n')

            if line.find('F') > -1:
                end = (line.find('F'), j)
            if line.find('I') > -1:
                start = (line.find('I'), j)
            j += 1

    x = len(lines[0])
    y = len(lines)

    return lines, start, end


def printMap(lines, actual):
    print()
    print()
    print()

    #print("\033[%d;%dH" % (0, 0)) # y, x

    for j in range(y):
        for i in range(x):
            if actual[0] == i and actual[1] == j:
                print('█', end='')
            else:
                print(lines[j][i], end='')

        print()


def get_value(c):
    v = -1

    if c == '.' or c == 'I' or c == 'F':
        v = 1
    elif c == 'X':
        v = -1

    return v


def get_char_from_map(mapa, coord):
    return mapa[coord[1]][coord[0]]


def get_value_from_map(mapa, coord):
    return get_value(get_char_from_map(mapa, coord))


def add_valid_pos(nb, mapa, coord):
    if get_value_from_map(mapa, coord) > -1:
        nb.append(coord)


def get_neighborhood(mapa, coord):
    nb = []
    if coord[0] == 0:
        add_valid_pos(nb, mapa, (coord[0] + 1, coord[1]))

    elif coord[0] == x - 1:
        add_valid_pos(nb, mapa, (coord[0] - 1, coord[1]))

    else:
        add_valid_pos(nb, mapa, (coord[0] + 1, coord[1]))
        add_valid_pos(nb, mapa, (coord[0] - 1, coord[1]))

    if coord[1] == 0:
        add_valid_pos(nb, mapa, (coord[0], coord[1] + 1))

    elif coord[1] == y - 1:
        add_valid_pos(nb, mapa, (coord[0], coord[1] - 1))

    else:
        add_valid_pos(nb, mapa, (coord[0], coord[1] + 1))
        add_valid_pos(nb, mapa, (coord[0], coord[1] - 1))

    return nb


mapa, start, end = read_file('Mapa10.txt')


def busca_largura(mapa):
    list_caminho:list = []
    list_vizitados:list = []
    testes:int = 0
    global start,end
    list_caminho.append((start,0))
    while len(list_caminho) > 0:
        testes += 1
        fronteira = list_caminho.pop(0)
        coord = fronteira[0]
        custo = fronteira[1]
        list_vizitados.append(coord)
        os.system('clear')
        printMap(mapa, coord)
        time.sleep(0.1)
        if coord == end:
            print("nós testados " + str(testes) + "\n")
            print("custo do caminho " + str(custo) + "\n")
            return
        for vizinho in get_neighborhood(mapa, coord):
            if vizinho not in list_vizitados:
                fx = custo + get_value_from_map(mapa, vizinho)
                list_caminho.append((vizinho,fx))



def busca_profundidade(mapa):
    list_caminho: list = []
    list_vizitados: list = []
    testes: int = 0
    global start, end
    list_caminho.append((start, 0))
    while len(list_caminho) > 0:
        testes += 1
        fronteira = list_caminho.pop()
        coord = fronteira[0]
        custo = fronteira[1]
        list_vizitados.append(coord)
        os.system('clear')
        printMap(mapa, coord)
        time.sleep(0.1)
        if coord == end:
            print("nós testados " + str(testes) + "\n")
            print("custo do caminho " + str(custo) + "\n")
            return
        for vizinho in get_neighborhood(mapa, coord):
            if vizinho not in list_vizitados:
                fx = custo + get_value_from_map(mapa, vizinho)
                list_caminho.append((vizinho, fx))


def manhattan_distance(_from, to):
    # |x2 - x1| + |y2 - y1|
    return abs(to[0] - _from[0]) + abs(to[1] - _from[1])


def busca_a_estrela(mapa):
    list_caminho = PriorityQueue()
    list_vizitados: list = []
    testes: int = 0
    global start, end
    list_caminho.put(0,(start, 0))
    while list_caminho:
        testes += 1
        fronteira = list_caminho.get()
        distancia_atual = fronteira[1][0]
        coord = fronteira[1][1]
        list_vizitados.append(coord)
        os.system('clear')
        printMap(mapa, coord)
        time.sleep(0.1)
        if coord == end:
            print("nós testados " + str(testes) + "\n")
            print("custo do caminho " + str(custo) + "\n")
            return
        for vizinho in get_neighborhood(mapa, coord):
            if vizinho not in list_vizitados:
                gx = manhattan_distance(vizinho, end)
                hx = get_value_from_map(mapa, vizinho)
                fx = gx + hx
                list_caminho.append(fx,(vizinho, fx))

busca_largura(mapa)
#busca_profundidade(mapa)
# busca_a_estrela(mapa)