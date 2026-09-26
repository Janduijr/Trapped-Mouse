class Labirinto:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.matriz = []
        self.erro = False
        self.caminho = []
        self._ler_labirinto()
        
    def resultado(self):
        resultado = self.resolver()
        if self.erro:
            print('O LABIRINTO É INVALIDO!')
            return
        else:
            if resultado:
                emojis = {'1': '🟫', '0': '⬜', '.': '🔴', 'm': '🐭', 'e': '🧀', '*': '🟢'}

                matriz_visual = [linha[:] for linha in self.matriz]

                for (l, c) in self.caminho:
                    if matriz_visual[l][c] not in ('m', 'e'):
                        matriz_visual[l][c] = '*'

                for l in range(0, len(matriz_visual)):
                    for c in range(0, len(matriz_visual[0])):
                        print(emojis[matriz_visual[l][c]], end='')
                    print('')
                
                print('PASSOS:', self.caminho)
            else:
                print("LABIRINTO SEM SAIDA!")
            
            
    def resolver(self):
        mouse = self._encontrar('m')
        if mouse is None:
            return False
        return self._backtrack(mouse[0], mouse[1])
        
    def _encontrar(self, caracter):
        for l in range(0, len(self.matriz)):
            for c in range(0, len(self.matriz[0])):
                if self.matriz[l][c] == caracter:
                    return (l,c)

    def _backtrack(self, linha, coluna):
        #BASE
        if self.matriz[linha][coluna] == "1":
            return False
        
        if self.matriz[linha][coluna] == ".":
            return False
        
        if self.matriz[linha][coluna] == 'e':
            self.caminho.append((linha,coluna))
            return True
        
        #MARCACAO
        original = self.matriz[linha][coluna]
        self.matriz[linha][coluna] = '.'
        self.caminho.append((linha,coluna))
    
        #ANDANDO
        
        if self._backtrack(linha, coluna + 1):  # direita
            return True
        if self._backtrack(linha, coluna - 1):  # esquerda
            return True
        if self._backtrack(linha + 1, coluna):  # baixo
            return True
        if self._backtrack(linha - 1, coluna):  # cima
            return True
        
        self.caminho.pop()
        
        return False
        

    def _ler_labirinto(self):
        with open(self.nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            
        for linha in linhas:
            linha = linha.strip()
            
            if linha == '':
                continue
            linha_atual = []
            for caractere in linha:
                caractere = caractere.lower()
                if caractere in ('0', '1', 'm', 'e'):
                    linha_atual.append(caractere)
                        
                else:
                    self.erro = True
            
            self.matriz.append(linha_atual)
        
        num_colunas = len(self.matriz[0])+2 if self.matriz else 0
        
        #add paredes
            
        for x in range(0,len(self.matriz)):
            self.matriz[x] = ['1'] + self.matriz[x] + ['1']
        
        parede = ['1'] * num_colunas
        self.matriz.insert(0, parede)
        self.matriz.append(parede)  

lab1 = Labirinto('labirinto.txt')
lab1.resultado()