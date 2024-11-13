# UMC - Avaliação Software Basico
# Nome: João Pedro Vicente
# Curso: Engenharia de Software
# Função que calcula o valor da diária conforme a quantidade de pessoas e o tipo de apartamento

import os
os.system("cls")
def calcular_diaria(qtd_pessoas, tipo_apartamento):
    if tipo_apartamento == 1:
        if qtd_pessoas == 1:
            diaria = 20.00
        elif qtd_pessoas == 2:
            diaria = 28.00
        elif qtd_pessoas == 3:
            diaria = 35.00
        elif qtd_pessoas == 4:
            diaria = 42.00
        elif qtd_pessoas == 5:
            diaria = 48.00
        elif qtd_pessoas == 6:
            diaria = 53.00
        else:
            diaria = None
    elif tipo_apartamento == 2:
        if qtd_pessoas == 1:
            diaria = 25.00
        elif qtd_pessoas == 2:
            diaria = 34.00
        elif qtd_pessoas == 3:
            diaria = 42.00
        elif qtd_pessoas == 4:
            diaria = 50.00
        elif qtd_pessoas == 5:
            diaria = 57.00
        elif qtd_pessoas == 6:
            diaria = 63.00
        else:
            diaria = None
    else:
        diaria = None
    return diaria

# Função para exibir o menu de preços
def exibir_menu():
    print("Menu de Preços:")
    print("Quantidade de Pessoas  |  Tipo 1 (R$)  |   Tipo 2 (R$)    |")
    print("----------------------------------------------------------")
    print("1 pessoa               |      20,00     |    25,00       |")
    print("2 pessoas              |      28,00     |     34,00      |")
    print("3 pessoas              |      35,00     |     42,00      |")
    print("4 pessoas              |      42,00     |     50,00      |")
    print("5 pessoas              |      48,00     |     57,00      |")
    print("6 pessoas              |      53,00     |     63,00      |")
    print("----------------------------------------------------------\n")

# Loop principal do programa
while True:
    # Exibir o menu de preços
    exibir_menu()

    try:
        # Entrada de dados
        try:
            qtd_pessoas = int(input("Informe a quantidade de pessoas (1 a 6): "))
            if not (1 <= qtd_pessoas <= 6):
                print("Erro: Quantidade de pessoas inválida. Deve ser entre 1 e 6.")
                continue  # Reinicia o loop para pedir as entradas novamente
        except ValueError:
            print("Erro: Entrada inválida. Você deve inserir um número para a quantidade de pessoas.")
            continue  # Reinicia o loop para pedir as entradas novamente

        try:
            tipo_apartamento = int(input("Informe o tipo de apartamento (1 ou 2): "))
            if not (tipo_apartamento == 1 or tipo_apartamento == 2):
                print("Erro: Tipo de apartamento inválido. Deve ser 1 ou 2.")
                continue  # Reinicia o loop para pedir as entradas novamente
        except ValueError:
            print("Erro: Entrada inválida. Você deve inserir um número para o tipo de apartamento.")
            continue  # Reinicia o loop para pedir as entradas novamente

        try:
            dias = int(input("Informe o número de dias de permanência: "))
            if dias <= 0:
                print("Erro: O número de dias deve ser maior que 0.")
                continue  # Reinicia o loop para pedir as entradas novamente
        except ValueError:
            print("Erro: Entrada inválida. Você deve inserir um número para os dias de permanência.")
            continue  # Reinicia o loop para pedir as entradas novamente

        # Cálculo da diária
        diaria = calcular_diaria(qtd_pessoas, tipo_apartamento)
        if diaria is not None:
            total = diaria * dias
            # Saída de dados
            print(f"O valor total da estadia é: R$ {total:.2f}")
        else:
            print("Erro: Tipo de apartamento inválido.")
       
        # Pergunta ao usuário se ele quer repetir o processo
        repetir = input('''Deseja fazer outro cálculo? 
                        [S] Sim
                        [N] Não
                        ''')
        if repetir != 's' and repetir != 'S':
            print("Encerrando o programa.")
            break  # Sai do loop e encerra o programa

    except ValueError:
        print("Erro: Por favor, insira os dados corretamente.")