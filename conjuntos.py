arquivo = "ex3.txt"
txt = open(arquivo, 'r')
i = 0

def uniao():
    conjunto1 = txt.readline()
    conjunto2 = txt.readline()
    resultado = conjunto1 + ", " + conjunto2
    print("União: conjunto 1 {"+conjunto1.replace('\n', '')+"}, conjunto 2 {"+conjunto2.replace('\n', '')+"}. Resultado: {"+resultado.replace('\n', '')+"}")

def intersecao():
    conjunto1 = txt.readline().replace('\n', '').replace(' ', '').split(',')
    conjunto2 = txt.readline().replace('\n', '').replace(' ', '').split(',')
    resultadoaux = []
    for j in conjunto1:
        for k in conjunto2:
            if j == k:
                resultadoaux.append(j)
    resultado = ''.join(str(caracter+", ") for caracter in resultadoaux)
    resultado = resultado[:-2]
    conjunto1print = str(conjunto1).replace('\n', '').replace('[', '').replace(']', '').replace("'", '')
    conjunto2print = str(conjunto2).replace('\n', '').replace('[', '').replace(']', '').replace("'", '')
    print("Interseção: conjunto 1 {"+conjunto1print+"}, conjunto 2 {"+conjunto2print+"}. Resultado: {"+resultado.replace('\n', '')+"}")

def diferenca():
    conjunto1 = txt.readline().replace('\n', '').replace(' ', '').split(',')
    conjunto2 = txt.readline().replace('\n', '').replace(' ', '').split(',')
    resultadoaux = []
    for j in conjunto1:
        if j not in conjunto2:
            resultadoaux.append(j)
    for k in conjunto2:
        if k not in conjunto1 and k not in resultadoaux:
            resultadoaux.append(k)
    resultado = ''.join(str(caracter+", ") for caracter in resultadoaux)
    resultado = resultado[:-2]
    conjunto1print = str(conjunto1).replace('\n', '').replace('[', '').replace(']', '').replace("'", '')
    conjunto2print = str(conjunto2).replace('\n', '').replace('[', '').replace(']', '').replace("'", '')
    print("Diferença: conjunto 1 {"+conjunto1print+"}, conjunto 2 {"+conjunto2print+"}. Resultado: {"+resultado.replace('\n', '')+"}")

def cartesiano():
    conjunto1 = txt.readline().replace('\n', '').replace(' ', '').split(',')
    conjunto2 = txt.readline().replace('\n', '').replace(' ', '').split(',')
    resultadoaux = []
    for j in conjunto1:
        for k in conjunto2:
            resultadoaux.append("("+j+","+k+")")
    resultado = ''.join(str(caracter + ", ") for caracter in resultadoaux)
    resultado = resultado[:-2]
    conjunto1print = str(conjunto1).replace('\n', '').replace('[', '').replace(']', '').replace("'", '')
    conjunto2print = str(conjunto2).replace('\n', '').replace('[', '').replace(']', '').replace("'", '')
    print("Produto cartesiano: conjunto 1 {" + conjunto1print + "}, conjunto 2 {" + conjunto2print + "}. Resultado: {" + resultado.replace('\n', '') + "}")

num_operacoes = txt.readline()
while i < int(num_operacoes):
    tipo = txt.readline()
    if tipo.replace('\n', '') == "U":
        uniao()
        i += 1
    elif tipo.replace('\n', '') == 'I':
        intersecao()
        i += 1
    elif tipo.replace('\n', '') == 'D':
        diferenca()
        i += 1
    elif tipo.replace('\n', '') == 'C':
        cartesiano()
        i += 1
    else:
        print("Formatação inválida")
        i += 1




