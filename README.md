# 🐭 Trapped Mouse — Labirinto com Backtracking

Programa em Python que lê um labirinto de um arquivo de texto e usa o algoritmo de **Backtracking** (busca com retrocesso) para encontrar o caminho de um rato (`m`) até a saída (`e`).

## Como funciona

O algoritmo tenta, recursivamente, mover o rato em uma direção. Se aquela direção levar a um beco sem saída (parede ou célula já visitada), o programa **desfaz o passo** (retrocede) e tenta outra direção — daí o nome *backtracking*.

Passos gerais:

1. Localiza a posição inicial do rato (`m`) na matriz.
2. Tenta se mover em ordem: **direita → esquerda → baixo → cima**.
3. Marca cada célula visitada com `.` para não entrar em loop infinito.
4. Se encontrar a saída (`e`), retorna sucesso e guarda o caminho percorrido.
5. Se nenhuma direção funcionar a partir de uma célula, remove essa célula do caminho (`pop()`) e retorna para a chamada anterior tentar outra direção.

## Formato do arquivo `labirinto.txt`

O arquivo deve conter apenas os caracteres:

| Caractere | Significado           |
|-----------|------------------------|
| `0`       | Caminho livre           |
| `1`       | Parede                  |
| `m`       | Posição inicial (mouse) |
| `e`       | Saída (exit)             |

Exemplo:

```
1100
000e
00m1
```

Não é necessário desenhar a borda externa do labirinto — o programa adiciona automaticamente uma parede (`1`) ao redor de toda a matriz ao carregar o arquivo.

Qualquer caractere fora desse conjunto (ignorando maiúsculas/minúsculas) marca o labirinto como inválido (`self.erro = True`).

## Como executar

1. Crie um arquivo `labirinto.txt` na mesma pasta do script, seguindo o formato acima.
2. Rode o script:

```bash
python trapped_mouse.py
```

3. O resultado é impresso no terminal com emojis:

| Emoji | Significado                              |
|-------|-------------------------------------------|
| 🟫    | Parede                                     |
| ⬜    | Caminho livre (não visitado)               |
| 🔴    | Célula visitada, mas que era um beco sem saída |
| 🟢    | Célula que faz parte do caminho até a saída |
| 🐭    | Posição inicial do rato                    |
| 🧀    | Saída                                      |

Se não existir nenhum caminho possível entre `m` e `e`, o programa exibe:

```
LABIRINTO SEM SAIDA!
```

## Estrutura do código

| Método            | Responsabilidade                                                        |
|--------------------|--------------------------------------------------------------------------|
| `_ler_labirinto`   | Lê o arquivo, valida os caracteres e adiciona as paredes externas.       |
| `_encontrar`       | Procura a posição de um caractere específico (`m` ou `e`) na matriz.     |
| `resolver`         | Ponto de entrada do algoritmo: localiza o mouse e inicia o backtracking. |
| `_backtrack`       | Implementa a busca recursiva com retrocesso (backtracking).             |
| `resultado`        | Executa a resolução e exibe o labirinto formatado com emojis.           |
