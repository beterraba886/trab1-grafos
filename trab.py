import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

class Estacao:
    #nome;
    #x;
    #y;

    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y

cores=['#ffbf00', '#0039e6', '#b300b3', '#ff6600', '#339933', '#739900', '#663300'] #linhas cores
ind = {} #ind das estacoes
estacoes = {} #mapa das estacoes

adj = []


def lerEstacoes():
    in_estacoes = open('in_estacoes.txt', 'r');
    count = 0
    coord_x = []
    coord_y = []
    nomes = []
    for line in in_estacoes:
        nome = line.split('>')[0]
        x = line.split('>')[1]
        y = line.split('>')[2]
        estacao = Estacao(nome, int(x), int(y))
        ind[nome] = count
        estacoes[nome] = estacao
        adj.append([])
        coord_x.append(int(x))
        coord_y.append(int(y))
        nomes.append(nome)
        count +=1
    
    ax.scatter(coord_x, coord_y, marker='o')
    for i, txt in enumerate(nomes):
        ax.text(coord_x[i]+1, coord_y[i], txt, fontsize=9)

def lerLinhas():
    in_linhas = open('in_linhas.txt', 'r');
    i = 0
    #7 pois sao 7 linhas
    while(i<7):
        line = in_linhas.readline().split()
        nome = line[0]
        cor = line[1]
        j = int(line[2])
        coord_x = []
        coord_y = []
        while(j>0):
            linha = in_linhas.readline().split('>')
            ind1 = ind.get(linha[0])
            #ind2 = ind.get(linha[1])
            estacao1 = estacoes.get(linha[0])
            estacao2 = estacoes.get(linha[1].replace('\n',''))
            adj[ind1].append(estacao2)
            coord_x.append(estacao1.x)
            coord_y.append(estacao1.y)
            if(j==1):
                coord_x.append(estacao2.x)
                coord_y.append(estacao2.y)
            j-=1
        ax.plot(coord_x, coord_y, color=cores[i])
        i +=1

lerEstacoes()
lerLinhas()
plt.show()