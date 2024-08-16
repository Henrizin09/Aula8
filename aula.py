# # Cadastro de clientes
# cliente1_nome = input("Digite o nome do cliente 1: ")
# cliente1_idade = int(input("Digite a idade do cliente 1: "))

# cliente2_nome = input("Digite o nome do cliente 2: ")
# cliente2_idade = 0
# if cliente2_nome:
#     cliente2_idade = int(input("Digite a idade do cliente 2: "))

# cliente3_nome = input("Digite o nome do cliente 3: ")
# cliente3_idade = 0
# if cliente3_nome:
#     cliente3_idade = int(input("Digite a idade do cliente 3: "))

# # Escolha dos quartos
# # Preços dos quartos
# preco_simples = 100
# preco_duplo = 150
# preco_luxo = 250

# # Cliente 1
# print("\nEscolha o tipo de quarto para o cliente 1:")
# print("1. Simples")
# print("2. Duplo")
# print("3. Luxo")
# cliente1_quarto = int(input("Digite o número do quarto escolhido: "))

# # Cliente 2
# if cliente2_nome:
#     print("\nEscolha o tipo de quarto para o cliente 2:")
#     print("1. Simples")
#     print("2. Duplo")
#     print("3. Luxo")
#     cliente2_quarto = int(input("Digite o número do quarto escolhido: "))

# # Cliente 3
# if cliente3_nome:
#     print("\nEscolha o tipo de quarto para o cliente 3:")
#     print("1. Simples")
#     print("2. Duplo")
#     print("3. Luxo")
#     cliente3_quarto = int(input("Digite o número do quarto escolhido: "))

# # Número de dias de estadia
# print("\nDigite o número de dias que cada cliente ficará no hotel:")

# cliente1_dias = int(input("Dias do cliente 1: "))
# if cliente2_nome:
#     cliente2_dias = int(input("Dias do cliente 2: "))
# if cliente3_nome:
#     cliente3_dias = int(input("Dias do cliente 3: "))

# # Cálculo do valor total da estadia
# # Cliente 1
# if cliente1_quarto == 1:
#     cliente1_preco_diaria = preco_simples
# elif cliente1_quarto == 2:
#     cliente1_preco_diaria = preco_duplo
# elif cliente1_quarto == 3:
#     cliente1_preco_diaria = preco_luxo
# else:
#     cliente1_preco_diaria = 0

# cliente1_valor_total = cliente1_preco_diaria * cliente1_dias

# # Cliente 2
# if cliente2_nome:
#     if cliente2_quarto == 1:
#         cliente2_preco_diaria = preco_simples
#     elif cliente2_quarto == 2:
#         cliente2_preco_diaria = preco_duplo
#     elif cliente2_quarto == 3:
#         cliente2_preco_diaria = preco_luxo
#     else:
#         cliente2_preco_diaria = 0

#     cliente2_valor_total = cliente2_preco_diaria * cliente2_dias

# # Cliente 3
# if cliente3_nome:
#     if cliente3_quarto == 1:
#         cliente3_preco_diaria = preco_simples
#     elif cliente3_quarto == 2:
#         cliente3_preco_diaria = preco_duplo
#     elif cliente3_quarto == 3:
#         cliente3_preco_diaria = preco_luxo
#     else:
#         cliente3_preco_diaria = 0

#     cliente3_valor_total = cliente3_preco_diaria * cliente3_dias

# # Exibição dos valores a serem pagos
# print("\nValores a serem pagos:")
# print(f"Cliente 1 ({cliente1_nome}): R$ {cliente1_valor_total:.2f}")
# if cliente2_nome:
#     print(f"Cliente 2 ({cliente2_nome}): R$ {cliente2_valor_total:.2f}")
# if cliente3_nome:
#     print(f"Cliente 3 ({cliente3_nome}): R$ {cliente3_valor_total:.2f}")

# aula 8