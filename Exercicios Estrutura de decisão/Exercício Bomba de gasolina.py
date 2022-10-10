# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
#
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro
#
# Escreva um algoritmo que leia o número de litros vendidos,
#  o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a
#  ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

# Passo 1: Perguntar se foi A (álcool) ou G (gasolina);

combustivel = str(input('Qual combustível (A-Álcool; G-Gasolina)? ')).upper()

precoa = float(1.9)

precog = float(2.5)

while combustivel != 'A' and combustivel != 'G':
    print('Favor preencher com "A" para álcool ou "G" para gasolina.')
    combustivel = str(input('Qual combustível (A-Álcool; G-Gasolina)? ')).upper()

# Passo 2: Perguntar a litragem abastecida;

validalitros = False

while not validalitros:

    try:
        litros_abastecidos = float(input('Quantos litros foram abastecidos? '))
        while litros_abastecidos <= 0:
            print('Favor digitar a litragem abastecida numericamente e acima de zero. Tente novamente.')
            litros_abastecidos = float(input('Quantos litros foram abastecidos? '))
        validalitros = True
    except ValueError:
        print('Favor digitar a litragem abastecida numericamente e acima de zero. Tente novamente.')

# Passo 3: Se for A e acima de 20l, aplicar desconto de 5% por litro;

if combustivel == 'A' and litros_abastecidos > 20:
    desc = float(litros_abastecidos * precoa * 0.05)
    print(f'''Você abasteceu com álcool. O preço total sem desconto é de R$ {precoa * litros_abastecidos:_.2f}.
Com desconto fica R$ {(precoa * litros_abastecidos) - desc:_.2f}, desconto de R$ {desc:_.2f}'''.replace('.', ',').replace('_', '.'))

# Passo 4: Se for G e acima de 20l, aplicar desconto de 6% por litro;

elif combustivel == 'G' and litros_abastecidos > 20:
    desc = float(litros_abastecidos * precog * 0.06)
    print(f'''Você abasteceu com gasolina. O preço total sem desconto é de R$ {precog * litros_abastecidos:_.2f}.
Com desconto fica R$ {(precog * litros_abastecidos) - desc:_.2f}, desconto de R$ {desc:_.2f}'''.replace('.', ',').replace('_', '.'))

# Passo 5: Se for G e até 20l, aplicar desconto de 4%;

elif combustivel == 'G' and litros_abastecidos > 0:
    desc = float(litros_abastecidos * precog * 0.04)
    print(f'''Você abasteceu com gasolina. O preço total sem desconto é de R$ {precog * litros_abastecidos:_.2f}.
Com desconto fica R$ {(precog * litros_abastecidos) - desc:_.2f}, desconto de R$ {desc:_.2f}'''.replace('.', ',').replace('_', '.'))

# Passo 6: Se for A e até 20l, aplicar desconto de 3% por litro;
elif combustivel == 'A' and litros_abastecidos > 0:
    desc = float(litros_abastecidos * precoa * 0.03)
    print(f'''Você abasteceu com álcool. O preço total sem desconto é de R$ {precoa * litros_abastecidos:_.2f}.
Com desconto fica R$ {(precoa * litros_abastecidos) - desc:_.2f}, desconto de R$ {desc:_.2f}'''.replace('.', ',').replace('_', '.'))
