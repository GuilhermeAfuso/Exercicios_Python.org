# Exercício 28 - Estrutura de decisão  - Hipermercado Tabajara - Python.org

# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
# porém não há limites para a quantidade de carne por cliente. Se a compra for feita no cartão Tabajara o
# cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo
# e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

#############################################//#####################################################

# Passo 1: Listar todos os produtos e tabelas de preços de cada produto.

carnes = ['file duplo', 'alcatra', 'picanha']

ate5 = ['4.9', '5.9', '6.9']

acima5 = ['5.8', '6.8', '7.8']

print('#' * 20, 'Seja bem-vindo(a)!', '#' * 20)

# Passo 2: O cliente deve informar se é ou não cliente do Hipermercado Tabajara.

clientefidelidade = str(input('Você é cliente Tabajara (S ou N)? ')).upper()

while clientefidelidade != 'S' and clientefidelidade != 'N':
    print('Favor digitar "S" para Sim e "N" para Não.')
    clientefidelidade = str(input('Você é cliente Tabajara (S ou N)? ')).upper()

print(clientefidelidade)

# Passo 3: O consumidor deve informar qual carne deseja comprar.

carne_cliente = str(input('Informe qual carne deseja comprar (Filé Duplo, Alcatra ou Picanha): ')).casefold()
carne_cliente = str(carne_cliente)

print(carne_cliente)

# Passo 4: O consumidor deve informar o peso.

validapeso_carne = False

while not validapeso_carne:
    try:
        peso_carne = float(input('Informe o peso em Kg de carne: '))
        while peso_carne <= 0:
            print('Favor digitar um peso de carne maior que zero. Tente novamente.')
            peso_carne = float(input('Informe o peso em Kg de carne: '))
        validapeso_carne = True
    except ValueError:
        print('Favor digitar o peso da carne em Kg corretamente.')

# Passo 5: Criar as condições de carne com o peso informado para definir o valor de compra da carne.

# 5.1: Identificar a carne informada pelo cliente na tabela de carnes.

for i, carne in enumerate(carnes):
    total = peso_carne * float(acima5[i])
    if carne_cliente == carne:
        if clientefidelidade == 'S':
            if peso_carne > 5:
                desc = total * 0.05
                print(f'A carne {carne} está R$ {float(acima5[i]):_.2f} por Kilo.'.replace('.', ',').replace('_', '.'))
                print(f'Peso total: {peso_carne:_.2f} Kg'.replace('.', ',').replace('_', '.'))
                print(f'Desconto: R$ {desc:_.2f}'.replace('.', ',').replace('_', '.'))
                print(f'Total a pagar: R$ {total - desc:_.2f}'.replace('.', ',').replace('_', '.'))
            else:
                desc = peso_carne * float(ate5[i]) * 0.05
                print(f'A carne {carne} está R$ {ate5[i]:_.2f} por Kilo.'.replace('.', ',').replace('_', '.'))
                print(f'Peso total: {peso_carne:_.2f} Kg'.replace('.', ',').replace('_', '.'))
                print(f'Desconto: R$ {desc:_.2f}'.replace('.', ',').replace('_', '.'))
                print(f'Total a pagar: R$ {total - desc:_.2f}'.replace('.', ',').replace('_', '.'))
        else:
            if peso_carne > 5:
                print(f'A carne {carne} está R$ {acima5[i]:_.2f} por Kilo.'.replace('.', ',').replace('_', '.'))
                print(f'Peso total: {peso_carne:_.2f} Kg'.replace('.', ',').replace('_', '.'))
                print(f'Total a pagar: R$ {total:_.2f}'.replace('.', ',').replace('_', '.'))
            else:
                print(f'A carne {carne} está R$ {ate5[i]:_.2f} por Kilo.'.replace('.', ',').replace('_', '.'))
                print(f'Peso total: {peso_carne:_.2f} Kg'.replace('.', ',').replace('_', '.'))
                print(f'Total a pagar: R$ {total:_.2f}'.replace('.', ',').replace('_', '.'))

