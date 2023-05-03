print('escolha uma das opções a seguir.')
print('1.conto de fadas')
print('2.conto de Sci-fi')
print('3.conto de epoca')
escolha = int(input('Digite o número do conto que deseja:'))
if (escolha == 1):
    print('Você escolheu o conto de fadas!')
    print(' ')
    objeto = input('Digite o Nome um Objeto:')
    veiculo = input('Digite o Nome um Veiclo:')
    traje = input('Digite o Nome um Traje:')
    cor = input('Digite o Nome uma Cor:')

    print('\033c', end='')#Limpa Tudo que já foi escrito antes.
    print('========[conto de fadas]========')
    print(' ')
    print(f'Cinderela acorda virada no cão, ela decide matar sua madrasta e meias irmãs com {objeto},e após enterrá-las, para não ser pega, ela resolve fugir com um {veiculo}, entretanto no meio do caminho ela encontra com um príncipe que estava fugindo da cerimônia de casamento usando {traje} de cor {cor}, cinderela ajuda o príncipe a fugir e juntos saem da cidade, e ambos viviam fugindo para sempre.')
    print('~fim.')
if (escolha == 2):
    print('você escolheu o conto de ficção cientifica!')
if (escolha == 3):
    print('você escolheu o conto de época!')
