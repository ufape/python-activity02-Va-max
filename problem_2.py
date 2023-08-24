# -*- coding: utf-8 -*-

# YOUR FULL NAME
# UAG00098
# Problem Set 2 - Problem 2
# Description:

"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
Leia três valores de ponto flutuante A, B e C.
Digite o valor A: 
Digite o valor B:
Digite o valor C:

Processes:
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossível calcular.”, caso haja uma divisão por 0 ou raiz de numero negativo.

Output(s):
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossível calcular.". Caso contrário, imprima o resultado das raízes com 3 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo.
Exemplo 1:
R1 = -0.297
R2 = -2.712
"""


def main():
 
    valor = float(input("Digite o valor: "))

    if valor >= 0 and valor <= 25:
        print("Intervalo [0, 25]")
    elif valor > 25 and valor <= 50:
        print("Intervalo (25, 50]")
    elif valor > 50 and valor <= 75:
        print("Intervalo (50, 75]")
    elif valor > 75 and valor <= 100:
        print("Intervalo (75, 100]")
    else:
        print("Fora de intervalo.")


if __name__ == '__main__':
    main()
