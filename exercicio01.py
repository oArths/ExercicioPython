import math
def som():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = num1 + num2
    
    print("A soma dos números é:", resultado)
def sub():
    num1 = int(input("Digite o 1° numero: "))
    num2 = int(input("Digite o 2° numero: "))

    resultado = num1 - num2

    print("a diferença entre os numeros é: ", resultado)
def mut():
    num1 = int(input("Digite o 1° numero: "))
    num2 = int(input("Digite o 2° numero: "))

    resultado = num1 * num2

    print("o produto entre os numeros é: ", resultado)
def div():
    num1 = int(input("Digite o 1° numero: "))
    num2 = int(input("Digite o 2° numero: "))

    resultado = num1 / num2
    print("a divisão entre os numeros são: ", resultado)
def res():
    num1 = int(input("Digite o 1° numero: "))
    num2 = int(input("Digite o 2° numero: "))

    resultado = num1 % num2
    print("o resto da entre os numeros: ", resultado)
def qua():
    num1 = int(input("Digite o numero: "))

    resultado = num1 ** 2
    print("o quadrado é: ", resultado)
def quaWithMath():
    num1 = int(input("Digite o numero: "))

    resultado = math.sqrt(num1) 
    print("o quadrado é: ", resultado)
def abs():
    num1 = int(input("Digite o numero: "))

    resultado = abs(num1) 
    print("o quadrado é: ", resultado)

# Exercicio09
# 01
# a. 347 -> int 
# b. 2.71  -> float
# c. “347”  -> string
# d. 2+3j -> complex
# 02
num1, num2 = 10, 5

def mToCm(m):
    conversao = m * 100
    mensagem = str(m)+" em cm é:"+str(conversao)
    print(mensagem)
def raio():
    raio = float(input("Digite o raio: "))

    area = math.pow(raio,2) * math.pi

    print("a area do circulo é:", area)
def salMes():
    valor = float(input("Quanto você ganha por hora?: "))
    mes = int(input("Quantas horas você trabalha nesse mês?: "))

    resutado = mes * valor
    print("seu salario esse mês é:", resutado)

def celFa():
    f = float(input("Digite a temperatura em °F: "))

    c = f /32
    print("A temperatura m °C é: ", c)

celFa()
