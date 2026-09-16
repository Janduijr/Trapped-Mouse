def ler_documento():
    erro = False
    with open('arquivo.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        linhast = len(linhas[0].strip())
        colunast = len(linhas)
    
    matriz = []
    
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
                erro = True
        
        matriz.append(linha_atual)
        
        
    if erro == False:    
        print(matriz)
    else:
        print('Ha caracteres invalidos!')

ler_documento()