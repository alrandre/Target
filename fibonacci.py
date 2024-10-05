# """
# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo
# valor sempre será a soma dos 2 valores anteriores
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na
# linguagem que desejar onde, informado um número, ele calcule a
# sequência de Fibonacci e retorne uma mensagem avisando se o número
# informado pertence ou não a sequência.
# """

def fibo(n):
    """
    Função para calcular a sequência de Fibonacci de forma iterativa

    Args:
        n (int): Número máximo para a sequência
    Returns:
        vetor (list): Lista contendo a sequência de Fibonacci 
    """
    vetor = [0,1]
    for i in range(2,n+2):
        soma = vetor[i-1] + vetor[i-2]
        if soma > n:
            break
        else:
            vetor.append(soma)
    return vetor


def menu():
    """
    Função para mostrar o menu do programa
    """
    print("Para sair, digite '-1'.")
    x = int(input('Digite um número: '))
    while x != -1:
        vet = fibo(x)
        print("\nFibonacci = ", vet)
        if x in vet:
            print(f"O número {x} faz parte da sequência de Fibonacci")
        else:
            print(f"O número {x} NÃO faz parte da sequência de Fibonacci")
        print("\nPara SAIR, digite '-1'.")
        x = int(input('Digite um número: '))

    print("\nFinalizando o programa...")
# Execução do programa
menu()