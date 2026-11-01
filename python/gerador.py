import random
from estruturas import Pilha

def gerar(tamanho):
    mapa = [["#"] * tamanho for _ in range(tamanho)]
    pilha = Pilha()
    mapa[1][1] = "."
    pilha.inserir((1, 1))

    while not pilha.esta_vazia():
        r, c = pilha.remover()
        opcoes = []

        for dr, dc in [(-2, 0), (0, 2), (2, 0), (0, -2)]:
            nr = r + dr
            nc = c + dc
            if 1 <= nr <= tamanho - 2 and 1 <= nc <= tamanho - 2 and mapa[nr][nc] == "#":
                opcoes.append((dr, dc))

        if opcoes:
            dr, dc = random.choice(opcoes)
            mapa[r + dr // 2][c + dc // 2] = "."
            mapa[r + dr][c + dc] = "."
            pilha.inserir((r, c))
            pilha.inserir((r + dr, c + dc))

    mapa[1][1] = "S"
    mapa[tamanho - 2][tamanho - 2] = "E"
    return mapa


if __name__ == "__main__":
    for linha in gerar(51):
        print("".join(linha))