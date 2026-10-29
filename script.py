def in_num(texto):
    while True:
        try:
            entrada = input(texto)
            if entrada.strip() == "":
                raise ValueError("TA VAZIO DIGITA AI PARCERO")
            return float(entrada)
        except ValueError:
            print("Erro: Digite apenas números válidos (seu maldito)!")

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("APRENDE NÃO SE DIVIDE POR ZERO!!!")
        return None

if __name__ == "__main__":
    print("CalZErro Zalculador Zero Erros")
    print("Escolha a operação:")
    print("1 = Somar +")
    print("2 = Subtrair -")
    print("3 = Multiplicar *")
    print("4 = Dividir /")
    
    op = input("Digite o número da operação desejada (1|2|3|4): ")

    # Pede os dois números usando a função segura
    num1 = in_num("Digite o primeiro número: ")
    num2 = in_num("Digite o segundo número: ")

    # Executa a operação escolhida
    if op == "1":
        resultado = somar(num1, num2)
        print(f"somando da: {resultado}")
    elif op == "2":
        resultado = subtrair(num1, num2)
        print(f"A subtração é: {resultado}")
    elif op == "3":
        resultado = multiplicar(num1, num2)
        print(f"A multiplicação é: {resultado}")
    elif op == "4":
        resultado = dividir(num1, num2)
        if resultado is not None:
            print(f"A divisão fica: {resultado}")
    else:
        print("Opção inválida!")

    print("Acabou")
