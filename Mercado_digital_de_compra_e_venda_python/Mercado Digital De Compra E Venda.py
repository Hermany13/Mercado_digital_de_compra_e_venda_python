from time import strftime
from datetime import date
while True:
    print('\033[7;36;m--------BEM VINDO A NOSSA LOJA--------\033[0;;m')
    option = int(input('\033[4;36;m[1] Para se registrar\n[2] Para acessar seus dados\n[3] Para Catalogar produtos\n[4] Comprar\n\033[7;36;mDigite a Opção desejada:\033[0;;m'))



    #opção 1
    if option == 1:
        name = str(input('\n\033[4;34;mDigite Seu Nome:').strip())
        day = str(input('\n\033[4;34;mDigite sua data de Nascimento\nDia: ').strip())
        month = str(input('\n\033[4;34;mMês: ').strip())
        year = str(input('\n\033[4;34;mAno: ').strip())
        user = str(input('\n\n\033[4;35;mNome de Usuário:').strip())
        password = str(input('\n\033[4;35;mSua Senha:').strip())
    
        registro = open('Registro {}.txt'.format(user), 'w')
        registro.write('Senha: {}'.format(str(password)+'\n'))
        registro.write('Nome: {}\n'.format(name.capitalize()))
        registro.write('Data De Nascimento: {}/{}/{}\n'.format(day, month, year))
        registro.close()
        opcao = int(input('\n\033[1;32;m[1] Continuar\n\033[1;31;m[2] Sair\n\033[7;36;mQual a Opção desejada:'))
        if (opcao == 1):
            continue
        elif (opcao == 2):
            break


    #opção 2
    if option == 2:
        print('\n\033[7;;m------Entre na sua conta------\033[0;;m')
        user2 = str(input('Digite seu nome de usuário:'))
        password2 = str(input('Digite Sua Senha:'))
        lista1 = []
        print('\n\033[7;;m--------Dados do Usuário--------\033[0;;m')
        senhas2 = open('Registro {}.txt'.format(user2), 'r')
        for linhas in senhas2:
            linhas = linhas.split()
            lista1.append(linhas)
        senhas2.close()
        if password2 in lista1[0][1]:
            arquivo = open('Registro {}.txt'.format(user2), 'r')
            for linha in arquivo:
                linha = linha.rstrip()
                print(linha)
            arquivo.close()
            print('\033[7;;m-------------Fim----------------\033[0;;m')
        opcao = int(input('\n\033[1;32;m[1] Continuar\n[2]\033[1;31;m Sair\n\033[7;36;mQual a Opção desejada:'))
        if (opcao == 1):
            continue
        elif (opcao == 2):
            break

    #opção 3
    if option == 3:
        print('\n\033[7;;m------Entre na sua conta------\033[0;;m')
        user2 = str(input('Digite seu nome de usuário:'))
        password2 = str(input('Digite Sua Senha:'))
        lista1 = []
        senhas2 = open('Registro {}.txt'.format(user2), 'r')
        for linhas in senhas2:
            linhas = linhas.split()
            lista1.append(linhas)
        if password2 in lista1[0][1]:
            produtos_reg = []
            n_prod = int(input('\033[1;35;mDigite o Número de produtos que deseja Catalogar:'))
            for x in range (n_prod):
                prod = str(input('\033[1;35;mDigite o Nome do produto:'))
                price = str(input('\033[1;32;mDigite O preço do produto:R$'))
                print('\033[7;;m-----------Catalogado-----------\033[0;;m')
                produtos_reg.append(prod.capitalize())
                produtos_reg.append(price)
            produtos_dados = open('Produtos.txt','a')
            count = 0
            for x in produtos_reg:
                produtos_dados.write(produtos_reg[count]+'\n')
                count = count+1
            produtos_dados.close()
        else:print('\033[1;31;mUsuário ou Senha incorretos\n\033[1;30;mTente Novamente')
        opcao = int(input('\n\033[1;32;m[1] Continuar\n\033[1;31;m[2] Sair\n\033[7;36;mQual a Opção desejada:'))
        if (opcao == 1):
            continue
        elif (opcao == 2):
            break

    #opção 4
    if option == 4:
        print('\n\033[7;;m------Entre na sua conta------\033[0;;m')
        user2 = str(input('Digite seu nome de usuário:'))
        password2 = str(input('Digite Sua Senha:'))
        lista1 = []
        senhas2 = open('Registro {}.txt'.format(user2), 'r')
        for linhas in senhas2:
            linhas = linhas.split()
            lista1.append(linhas)
        if password2 in lista1[0][1]:
            catalogo = open('Produtos.txt', 'r')
            catalogo2 = []
            for produtos in catalogo:
                produtos = produtos.rstrip()
                catalogo2.append(produtos)
            catalogo.close()
            count = 0
            print('')
            for x in range (len(catalogo2)//2):
                print('{} R${}'.format(catalogo2[count], catalogo2[count+1]))
                count = count+2
            print('')
            prod = str(input('\033[1;30;mDigite o Nome do Produto que deseja comprar:'))
            if prod.capitalize() in catalogo2:
                quanti = int(input('\033[1;30;mQuantidade que deseja comprar:'))
                preco = float(catalogo2[(catalogo2.index(prod.capitalize())+1)])
                pagar = preco*quanti
                print('\033[1;32;mTotal:R${:.2f}'.format(pagar))
                registro = open('Registro {}.txt'.format(user2), 'a')
                registro.write('\n\nData da Compra:{}/{}/{}'.format(date.today().strftime('%d'), date.today().strftime('%m'), date.today().strftime('%Y')))
                registro.write('\nProduto Comprado:{}\nPreço:R${:.2f}\nTotal:R${:.2f}'.format(prod.capitalize(), preco, pagar))
                registro.close()
                print('\033[7;;m------Compra Finalizada------\033[0;;m')
                
            else:print('\033[1;31;mProduto Não Consta no Catalogo')
        else:print('\033[1;31;mUsuário ou Senha incorretos\n\033[1;30;mTente Novamente')
        opcao = int(input('\n\033[1;32;m[1] Continuar\n\033[1;31;m[2] Sair\n\033[7;36;mQual a Opção desejada:'))
        if (opcao == 1):
            continue
        elif (opcao == 2):
            break
