# Instrução, letra a do trabalho prático.
saida = ''

# Instrução, letra b do trabalho prático.
def adicao(a, b):
    return a+b

# Instrução, letra c do trabalho prático.
def subtracao(a, b):
    return a-b

# Instrução, letra d do trabalho prático.
def multiplicacao(a, b):
    return a*b

# Instrução, letra e do trabalho prático.
def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a/b

# Instrução, letra f ; g do trabalho prático.
def calculadora(num1, num2, operação):
    if operacao in ('+', 'adicao'):
        resultado = adicao(num1, num2)
    elif operacao in ('-', 'subtracao'):
        resultado = subtracao(num1, num2)
    elif operacao in ('*', 'multipicacao'):
        resultado = multiplicacao(num1, num2)
    elif operacao in ('/', 'divisao'):
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida!"

    return resultado

# Instrução, letra h ; i do trabalho prático.
while saida.lower() != 'n':
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a aperação desejada (+, -, *, / ou nome da operação): ").lower()

    resultado = calculadora(num1, num2, operacao)

    print(f"Resultado da operação: {resultado}")

    saida = input("Deseja continuar? (S/N): ").strip()