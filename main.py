class Labirinto:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.matriz = []
        self.erro = False
        self._ler_labirinto()
        

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
print(lab1.matriz)
