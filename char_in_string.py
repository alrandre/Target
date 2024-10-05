# 2) Escreva um programa que verifique, em uma string,
# a existência da letra ‘a’, seja maiúscula ou minúscula,
# além de informar a quantidade de vezes em que ela ocorre.

def menu():
    """
    Função para mostrar o menu do programa
    """
    print("Para sair, digite 'SAIR'.")
    palavra = input('Digite uma frase: ')
    while palavra.lower() != 'sair':
        if 'a' in palavra or 'A' in palavra:
            print(f"A letra 'A' aparece {palavra.count('a') + palavra.count('A')} vezes")
        else:
            print('A letra A não aparece nenhuma vez no texto digitado.')
        print("\nPara SAIR, digite 'SAIR'.")
        palavra = input('Digite uma frase: ')
    print("\nFinalizando o programa...")

# Execução do programa
menu()
