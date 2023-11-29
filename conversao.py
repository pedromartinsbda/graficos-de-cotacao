from moedas import converter_cotacao

def menu():
    print()
    print('1 - Converter Dolar em Real')
    print('2 - Converter Euro em Real')
    print('3 - Converter Libras em Real')
    print('4 - Outra cotação')
    print('0 - Sair')
    print()

opcao = 1

while opcao != 0:
    menu()
    opcao = int(input("Escolha uma opção: "))

    destino = 'BRL'
    valor = int(input("Digite o valor: "))

    match opcao:
        case 1: origem = "USD"
        case 2: origem = "EUR"
        case 3: origem = "GBP"
        case 4:
            origem = input("Digite a ORIGEM: ")
            destino = input("Digite o DESTINO: ")
    
    if opcao:
        print()
        print(f'{origem} para {destino}:', converter_cotacao(origem, destino, valor))
