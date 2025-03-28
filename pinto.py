def exercício1()
    nota = int(input("Digite a nota de 0 a 10"))
    if (nota >= 7):
        print("Aprovado")
    else:
        print("Reprovado")

def exercício2()
    if linguagem == "C++":
        print("C++ é uma linguagem de programção compilada.")
    
    elif linguagem == "Python":
        print("Python é uma linguagem de programação de alto nível")
    
    elif linguagem == "Java":
        print("Java é uma linguagem de programação amplamente utiizado no mercado")

    else:
        print("Não é nenhuma das três opções.")
exercício2()

def exercício3():
    media = float(input("Digite a média do aluno: "))
    percent = float(input("Digite o percentual de frequência"))

    if (percent < 75):
        print("Reprovado por falta.")
    elif(media < 6)
        print("Reprovado por nota")
    else():
        print("Aprovado")


def exercício4():
    diariatype = str(input("Digite o tipo da diária: "))
    numdiária = int(input("Digite o número de diárias: "))
    if diariatype.casefold() == "d":
        num = 255.90
        print("Tipo de diária S: \n Quarto Simples: ")
        print(f"Valor a pagar R$ {(num * numdiária):.2f}")
    elif diariatype.casefold() == "d":
        num = 305.50
        print("Tipo de diária S: \n Quarto Duplo: ")
        print(f"Valor a pagar R$ {(num * numdiária):.2f}")
    elif diariatype.casefold() == "d":
        num = 360.50
        print("Tipo de diária S: \n Quarto Triplo: ")
        print(f"Valor a pagar R$ {(num * numdiária):.2f}")
    else:
        print("tipo de diária invalido")

def exercício5()
    valor_original = float(input("Digite o valor da compra: R$ "))
    desconto = float(input("Desconto (em %) para essa compra: "))
    desconto = desconto / 100

    print('Valor original:    R$', valor_original)
    print('Desconto ganho:    R$', valor_original * desconto)
    print('Valor com desconto: R$', valor_original * (1-desconto))

def exercício6()
    placa = int(input("Digite os quarto digitos da placa"))
    final = placa % 10
    if final == 1 or final == 2:
        print("O veiculo não pode circular as segundas-feiras")
    elif final == 3 or final == 4:
        print("O veiculo não pode circular as Terças-feiras")
    elif final == 5 or final == 6:
        print("O veiculo não pode circular as Quartas-feiras")
    elif final == 7 or final == 8:
        print("O veiculo não pode circular as Quintas-feiras")
    else:
        print("O veiculo não pode circular as Sextas-feiras")


