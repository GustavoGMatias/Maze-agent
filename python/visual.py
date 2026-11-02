import tkinter as tk
from gerador import gerar_passos
from agente import agente
from estruturas import Pilha, Fila

TAMANHO = 31
CASA = 18
CORES = {"#": "#1e1e2e", ".": "#f5f5f5", "S": "#2ecc71", "E": "#e74c3c", "*": "#3498db"}


class App:
    def __init__(self, janela):
        self.janela = janela
        janela.title("Labirinto")
        self.mapa = None
        self.ocupado = False

        lado = TAMANHO * CASA
        self.canvas = tk.Canvas(janela, width=lado, height=lado, highlightthickness=0)
        self.canvas.pack()

        self.retangulos = []
        self.exibido = [[None] * TAMANHO for _ in range(TAMANHO)]
        for r in range(TAMANHO):
            linha = []
            for c in range(TAMANHO):
                x, y = c * CASA, r * CASA
                linha.append(self.canvas.create_rectangle(x, y, x + CASA, y + CASA, fill=CORES["#"], outline=""))
            self.retangulos.append(linha)

        self.texto = tk.Label(janela, text="")
        self.texto.pack()

        barra = tk.Frame(janela)
        barra.pack(pady=6)
        tk.Button(barra, text="Novo labirinto", command=self.novo).pack(side="left", padx=4)
        tk.Button(barra, text="Resolver com DFS (pilha)", command=lambda: self.resolver(Pilha, "DFS")).pack(side="left", padx=4)
        tk.Button(barra, text="Resolver com BFS (fila)", command=lambda: self.resolver(Fila, "BFS")).pack(side="left", padx=4)

    def pintar(self, caminho=()):
        marcadas = set(caminho)
        for r in range(TAMANHO):
            for c in range(TAMANHO):
                ch = self.mapa[r][c]
                if (r, c) in marcadas and ch not in ("S", "E"):
                    ch = "*"
                if self.exibido[r][c] != ch:
                    self.canvas.itemconfig(self.retangulos[r][c], fill=CORES[ch])
                    self.exibido[r][c] = ch

    def novo(self):
        if self.ocupado:
            return
        self.ocupado = True
        self.texto.config(text="Gerando...")
        self.passos = gerar_passos(TAMANHO)
        self.animar()

    def animar(self):
        try:
            self.mapa = next(self.passos)
        except StopIteration:
            self.ocupado = False
            self.texto.config(text="Pronto. Escolhe DFS ou BFS.")
            return
        self.pintar()
        self.janela.after(10, self.animar)

    def resolver(self, estrutura, nome):
        if self.ocupado or self.mapa is None:
            return
        achou, visitadas, caminho = agente(self.mapa, estrutura())
        self.pintar(caminho)
        self.texto.config(text=f"{nome}: {visitadas} salas visitadas, caminho de {len(caminho)} salas")


if __name__ == "__main__":
    janela = tk.Tk()
    app = App(janela)
    app.novo()
    janela.mainloop()