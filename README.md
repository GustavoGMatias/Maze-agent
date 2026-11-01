# Meu primeiro agente: saindo de um labirinto

Um agente de IA simples que encontra o caminho da entrada até a saída de um labirinto. Fiz esse projeto pra juntar três coisas: lógica de agentes, estruturas de dados (pilha e fila) e prática de Python, e depois levar tudo pra C.

## Como rodar

```bash
cd python
python3 agente.py
```

O programa roda o agente duas vezes no mesmo labirinto, uma com pilha e outra com fila, e imprime se achou a saída, quantas salas visitou e o caminho.

## O mapa

```
##S.##
#...##
#.#..#
#...##
..##.E
#....#
```

`#` é parede, `.` é caminho livre, `S` é o início e `E` é a saída. Esse labirinto tem um beco sem saída e um ciclo, de propósito, pra o agente precisar de memória.

## Como funciona

O agente repete um ciclo: observa os vizinhos livres da sala atual, decide qual explorar e anda até ela. As salas que ainda faltam explorar ficam guardadas numa estrutura de dados, e é ela que define o comportamento:

- **Pilha (DFS, busca em profundidade):** sai a última sala que entrou. O agente mergulha num caminho até travar e só então volta. Acha *um* caminho, não necessariamente o mais curto.
- **Fila (BFS, busca em largura):** sai a sala mais antiga. O agente explora em ondas, primeiro tudo a 1 passo, depois a 2, e assim por diante. Sempre acha o caminho com menos passos.

O laço do agente é o mesmo nos dois casos. Só troca a estrutura que eu passo pra ele. Pra isso, `Pilha` e `Fila` têm os mesmos métodos: `inserir`, `remover` e `esta_vazia`.

Dois conjuntos de memória fazem o agente funcionar:

- `visitados`, um `set` com as salas que ele já viu, pra não girar em círculo no ciclo do mapa;
- `veio_de`, um dicionário que guarda, pra cada sala, de qual sala o agente veio. Quando chega na saída, eu sigo esses "bilhetes" de trás pra frente pra montar o caminho.

Resultado no mapa acima: a pilha visitou 16 salas e a fila visitou 19, e as duas chegaram à saída por um caminho de 12 salas.

## Estrutura do projeto

```
meu-primeiro-agente/
├── README.md
├── python/
│   ├── estruturas.py   # classes Pilha e Fila
│   └── agente.py       # mapa, vizinhos e o agente
└── c/                  # versão em C (em breve)
```

## O que aprendi

- Criar classes em Python do zero (`self`, `__init__`, métodos) e que cada objeto tem os seus próprios dados.
- Que a pilha e a fila só diferem em qual ponta da lista eu tiro o próximo item. Um bug meu, entrar e sair pela mesma ponta do `deque`, transformou minha fila numa pilha sem eu perceber.
- Que o papel conta a partir de 1 e o código a partir de 0. Esse deslocamento de 1 me pegou na hora de achar o `S`.
- Checar os limites do mapa antes de acessar `mapa[linha][coluna]`, pra não ler fora dele.
- Usar `set` pra lembrar onde já estive e dicionário pra lembrar de onde vim.
- Que DFS e BFS são o mesmo algoritmo com uma caixinha diferente.

## Próximos passos

- Reescrever as estruturas e o agente em C, com array e `struct`.
- Testar um labirinto maior.
