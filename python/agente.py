from estruturas import Pilha, Fila
import copy

mapa = [
       [ "#", "#", "S", ".", "#", "#"],
       [ "#", ".", ".", ".", "#", "#"],
       [ "#", ".", "#", ".", ".", "#"],
       [ "#", ".", ".", ".", "#", "#"],
       [ ".", ".", "#", "#", ".", "E"],
       [ "#", ".", ".", ".", ".", "#"]
]

def posicao(mapa,alvo):

    for r, linha in enumerate(mapa):
        for c, coluna in enumerate(linha):
            if coluna == alvo:
                return(r,c)
    return None

def vizinhos (mapa, pos):
    r, c = pos
    livres = []

    movimentos = [
        (-1, 0),  # cima 
        (0, 1),   # direita 
        (1, 0),   # baixo 
        (0, -1)   # esquerda 
    ]

    for dr, dc in movimentos:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < len(mapa) and 0 <= nc < len(mapa[0]) and mapa [nr][nc] != "#":
            livres.append((nr,nc)) 

    return livres

def agente (mapa, estrutura):
    inicio = posicao(mapa, "S")
    visitados = set()
    veio_de = {}
    veio_de[inicio] = None
    estrutura.inserir(inicio)
    visitados.add(inicio)

    while not estrutura.esta_vazia():
        atual = estrutura.remover()
        print(atual)


        if atual == posicao(mapa, "E"):
            caminho = []
            sala = atual
            while sala is not None:
                caminho.append(sala)
                sala = veio_de[sala]
            caminho.reverse()
            return True, len(visitados), caminho

        for vizinho in vizinhos(mapa, atual):

            if vizinho not in visitados:
                veio_de[vizinho] = atual
                visitados.add(vizinho)
                estrutura.inserir(vizinho)

    return False, len(visitados) 

def mostrar(mapa, caminho):
    copia = copy.deepcopy(mapa)
    for r, c in caminho:
        if copia[r][c] not in ("S", "E"):
            copia[r][c] = "*"
    for linha in copia:
        print("".join(linha))

if __name__ == "__main__":
    print("Saída no metodo de pilha:")
    print(agente(mapa, Pilha()))

    print("Saída no metodo de Fila:")
    print(agente(mapa, Fila()))
    achou, visitadas, caminho = agente(mapa, Fila())
    mostrar(mapa, caminho)