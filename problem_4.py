# -*- coding: utf-8 -*-

# YOUR FULL NAME
# UAG00098
# Problem Set 2 - Problem 3
# Description:

"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
Digite 6 valores inteiros quaisquer.
Exemplo:
Digite o valor 1/6: 2
Digite o valor 2/6: 3
Digite o valor 3/6: 4
Digite o valor 4/6: 5
Digite o valor 5/6: 6
Digite o valor 6/6: 7

Processes:
Faça um programa que leia 6 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Output(s):
Exemplo:
Você digitou 3 valores pares.
"""


def main():
    valor_1 = int(input("Digite o valor 1/6: "))
    valor_2 = int(input("Digite o valor 2/6: "))
    valor_3 = int(input("Digite o valor 3/6: "))
    valor_4 = int(input("Digite o valor 4/6: "))
    valor_5 = int(input("Digite o valor 5/6: "))
    valor_6 = int(input("Digite o valor 6/6: "))
    quantidade = 0
    if (valor_1 % 2) == 0:
        quantidade = quantidade + 1 # quantidade += 1
    if (valor_2 % 2) == 0:
        quantidade = quantidade + 1
    if (valor_3 % 2) == 0:
        quantidade = quantidade + 1
    if (valor_4 % 2) == 0:
        quantidade = quantidade + 1
    if (valor_5 % 2) == 0:
        quantidade = quantidade + 1  
    if (valor_6 % 2) == 0:
        quantidade = quantidade + 1
    print(f"Você digitou {quantidade} valores pares.")


if __name__ == '__main__':
    main()
