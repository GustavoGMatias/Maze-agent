from collections import deque

class Pilha:
    def __init__(self):
        self.itens = []

    def inserir(self, item):
        self.itens.append(item)

    def remover(self):
        return self.itens.pop()

    def esta_vazia(self):
        return len(self.itens) == 0

class Fila:
    def __init__(self):
        self.fila = deque()

    def inserir(self, item):
        self.fila.append(item)

    def remover(self):
        return self.fila.popleft()

    def esta_vazia(self):
        return len(self.fila) == 0




