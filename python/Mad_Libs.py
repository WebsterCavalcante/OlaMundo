print(' ')
print('Escolha Uma Das Opções a Seguir.')
print(' ')
print('1.conto de fadas')
print('2.conto de Sci-fi')
print('3.conto de epoca')
escolha = int(input('Digite o número do conto que deseja:'))
if (escolha == 1):
    print('\033c', end='')#Limpa Tudo que já foi escrito antes.
    print('Você escolheu o conto de fadas!')
    print(' ')
    objeto = input('Digite o Nome um Objeto:')
    veiculo = input('Digite o Nome um Veiclo:')
    traje = input('Digite o Nome um Traje:')
    cor = input('Digite o Nome uma Cor:')

    print('\033c', end='')#Limpa Tudo que já foi escrito antes.
    print('========[Conto De Fadas]========')
    print(' ')
    print(f'Cinderela acorda virada no cão, ela decide matar sua madrasta e meias irmãs com {objeto},e após enterrá-las, para não ser pega, ela resolve fugir com um {veiculo}, entretanto no meio do caminho ela encontra com um príncipe que estava fugindo da cerimônia de casamento usando {traje} de cor {cor}, cinderela ajuda o príncipe a fugir e juntos saem da cidade, e ambos viviam fugindo para sempre.')
    print(' ')
    print('~fim.')
if (escolha == 2):
    print('\033c', end='')#Limpa Tudo que já foi escrito antes.
    print('Você Escolheu o Conto De Ficção Cientifica!')
    nome_cap = input('Digite o Nome De Uma Pessoa: ')
    nome_eng = input('Digite o Nome De Uma Pessoa: ')
    nome_med = input('Digite o Nome De Uma Pessoa: ')
    alien = input('Digite o Nome De Uma criatura: ')

    print('\033c', end='')#Limpa Tudo que já foi escrito antes.
    print('========[Conto De Ficção Cientifica]========')
    print(' ')
    print(f'Uma nave espacial caiu em um planeta desconhecido os únicos sobreviventes são a capitã {nome_cap} a engenheira {nome_eng} e o medico {nome_med} juntos eles tentam consertar a nave, mas um(a) {alien} surge. a engenheira {nome_eng} consegue matar o(a) {alien}, mas o medico {nome_med} morre trajicamente, {nome_eng} e {nome_cap} continuaram vivas e após saírem do planeta viveram felizes para sempre.')
    print(' ')
    print('~fim.')
if (escolha == 3):
    print('você escolheu o conto de época!')
