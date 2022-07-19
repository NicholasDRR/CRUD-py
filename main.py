import os

from rich import print
from rich.prompt import Prompt
from rich.table import Table

from CRUD.validate import dao, func

# DECLARANDO VAR PRA RECEBER O PROMPT
prompt = Prompt()
# CRIANDO A FUNÇÃO LIMPA TELA
clear = lambda: os.system('cls')

# MENU INICIAL
func.less()
print('CRUD'.center(24))
func.less()
print('''[yellow]1: Inserir  3: Atualizar
2: Ler      4: Deletar[/]'''.center(24))
func.less()
opc = input('Digite sua opção: ')

while True:
    if opc in ('1', '2', '3', '4'):
        clear()
        # INSERT
        if opc == '1':
            func.title('INSERINDO DADOS')
            name = input('Nome: ')
            name_product = func.checkstr(name)
            while True:
                if name_product:
                    break
                else:
                    clear()
                    func.title('INSERINDO DADOS')
                    print('[red]:X: Por favor, digite apenas letras[/]')
                    name = input('Nome: ')
                    name_product = func.checkstr(name)
            number = input('Preço: ')
            price = func.checknumeric(func.convert(number))
            while True:
                if number[0] == '.':
                    clear()
                    func.title('INSERINDO DADOS')
                    print('[red]:X: Por favor digite o valor novamente![/]')
                    number = input('Preço: ')
                    price = func.checknumeric(func.convert(number))
                if price:
                    break
                else:
                    clear()
                    func.title('INSERINDO DADOS')
                    print('[red]:X: Por favor, digite apenas números[/]')
                    number = input('Preço: ')
                    price = func.checknumeric(func.convert(number))
            if name_product and price:
                nameexist = dao.insert(name, number)
                if nameexist:
                    func.bar('INSERINDO')
                    clear()
                    func.title('INSERINDO DADOS')
                    print(f'[red]:X: ERRO! (Nome de produto já existe)[/]')
                else:
                    try:
                        dao.insert(name, number)
                        func.bar('INSERINDO')
                        print('[green]:heavy_check_mark: Produto adicionado[/]')
                    except:
                        print('[red]:X: ERRO! (desconhecido)[/]')
        # READ
        if opc == '2':
            func.title('BANCO DE DADOS')
            tbl = input('Qual tabela deseja ver: ')
            table = func.checkstr(tbl)
            while True:
                if table:
                    clear()
                    tbl2 = tbl.upper()
                    try:
                        read = dao.read(tbl)
                        table = Table(title=f'[yellow]{tbl2}[/]', style='yellow')
                        table.add_column('Id_product')
                        table.add_column('Name_product')
                        table.add_column('Price')
                        for i in read:
                            table.add_row(str(i[0]), str(i[1]), str(i[2]))
                        func.bar('LENDO')
                        clear()
                        print(table)
                        break
                    except:
                        func.title('BANCO DE DADOS')
                        print('[red]:X: ERRO! (tabela desconhecida).[/]')
                        tbl = input('Qual tabela deseja ver: ')
                        table = func.checkstr(tbl)

                else:
                    clear()
                    func.title('BANCO DE DADOS')
                    print('[red]:X: Digite apenas letras.[/]')
                    tbl = input('Qual tabela deseja ver: ')
                    table = func.checkstr(tbl)
        # UPDATE
        if opc == '3':
            func.title('ATUALIZANDO VALORES')
            print('''1: Nome
2: Preço''')
            func.less()
            att = input('Atualizar: ')
            while True:
                if att == '1':
                    clear()
                    func.title('ATUALIZANDO DADOS')
                    nwname = input('Novo nome: ')
                    new_name = func.checkstr(nwname)
                    while True:
                        if new_name:
                            name = nwname
                            break
                        else:
                            clear()
                            func.title('ATUALIZANDO DADOS')
                            print('[red]:X: Digite apenas letras.[/]')
                            nwname = input('Novo nome: ')
                            new_name = func.checkstr(nwname)
                    idp = input('Id do produto: ')
                    id_product = func.checknumeric(idp)
                    while True:
                        if id_product:
                            newid = idp
                            break
                        else:
                            clear()
                            func.title('ATUALIZANDO DADOS')
                            print('[red]:X: Digite apenas números.[/]')
                            idp = input('Id do produto: ')
                            id_product = func.checknumeric(idp)
                    if new_name and id_product:
                        idexist = dao.id(newid)
                        nameexist = dao.name(nwname)
                        if nameexist or idexist:
                            func.bar('ATUALIZANDO')
                            clear()
                            func.title('ATUALIZANDO DADOS')
                            if nameexist:
                                print(f'[red]:X: ERRO! (Nome de produto já existe)[/]')
                            if idexist:
                                print(f'[red]:X: ERRO! (ID de produto inválido)[/]')
                        else:
                            dao.update(name, newid)
                            func.bar('ATUALIZANDO')
                            print('[green]:heavy_check_mark: Nome atualizado![/]')
                    break
                elif att == '2':
                    clear()
                    func.title('ATUALIZANDO DADOS')
                    np = input('Novo preço: ')
                    new_price = func.checknumeric(func.convert(np))
                    while True:
                        if np[0] == '.':
                            clear()
                            func.title('ATUALIZANDO DADOS')
                            print('[red]:X: Por favor digite o valor novamente![/]')
                            np = input('Novo Preço: ')
                            new_price = func.checknumeric(func.convert(np))
                        if new_price:
                            break
                        else:
                            clear()
                            func.title('ATUALIZANDO DADOS')
                            print('[red]:X: Digite apenas números[/]')
                            np = input('Novo Preço: ')
                            new_price = func.checknumeric(func.convert(np))
                    idp = input('Id do produto: ')
                    id_product = func.checknumeric(idp)
                    while True:
                        if id_product:
                            break
                        else:
                            clear()
                            func.title('ATUALIZANDO DADOS')
                            print('[red]:X: Digite apenas números.[/]')
                            idp = input('Id do produto: ')
                            id_product = func.checknumeric(idp)
                    if new_price and id_product:
                        idexist = dao.id(idp)
                        if idexist:
                            clear()
                            func.title('ATUALIZANDO DADOS')
                            func.bar('ATUALIZANDO')
                            print(f'[red]:X: ERRO! (ID de produto inválido)[/]')
                        else:
                            try:
                                dao.update(np, idp)
                                func.bar('ATUALIZANDO')
                                print('[green]:heavy_check_mark: Preço atualizado[/]! ')
                            except Exception as error:
                                print('[red]:X: ERRO (desconhecido)[/]')
                                print(f'{error}')
                    break
                else:
                    clear()
                    func.title('ATUALIZANDO DADOS')
                    print('[red]:X: Escolha entre [blue]1[/] e [blue]2[/][/]')
                    att = input('Atualizar: ')
                # DELETE
        # DELETE
        if opc == '4':
            clear()
            func.title('DELETANDO DADOS')
            nm = input('Deseja apagar quantos valores: ')
            amount = func.checknumeric(nm)
            while True:
                if amount:
                    while True:
                        if nm == '1':
                            clear()
                            func.title('DELETANDO DADOS')
                            id = input('Id do produto: ')
                            id_product = func.checknumeric(id)
                            while True:
                                if id_product:
                                    idexist = dao.delete(id)
                                    try:
                                        if idexist:
                                            func.bar('DELETANDO')
                                            print(
                                                f'[green]:heavy_check_mark: Produto com id: [blue]{id}[/] deletado![/]')
                                            break
                                        else:
                                            func.bar('DELETANDO')
                                            clear()
                                            func.title('DELETANDO DADOS')
                                            print('[red]:X: ERRO (ID inexistente).[/]')
                                            break
                                    except Exception as erro:
                                        print('[red]:X: ERRO! Digite um id válido.[/]')
                                        print(erro)
                                else:
                                    clear()
                                    func.title('DELETANDO DADOS')
                                    print('[red]:X: Digite apenas números.[/]')
                                    id = input('Id do produto: ')
                                    id_product = func.checknumeric(id)
                            break
##################################################
                        elif int(nm) > 1:
                            clear()
                            func.title('DELETANDO DADOS')
                            id_product = []
                            c = 0
                            while True:
                                if int(c) >= int(nm):
                                    break
                                np = prompt.ask(f'[blue]{c + 1}º[/] id')
                                number = func.checknumeric(np)
                                if number:
                                    id_product.append(np)
                                    idnotexist = dao.id(np)
                                    if idnotexist:
                                        print('teste')
                                        break
                                    else:
                                        for ids in id_product:
                                            dao.delete(ids)
                                        func.bar('DELETANDO')
                                        print(f'[green]:heavy_check_mark: Id [blue]{np}[/] deletado![/]')
                                else:
                                    #c = -1
                                    clear()
                                    func.title('DELETANDO DADOS')
                                    print('[red]:X: Digite um id válido[/]')
                                c += 1
                            break
                        else:
                            clear()
                            func.title('DELETANDO DADOS')
                            print('[red]:X: Número inválido[/]')
                            nm = input('Deseja apagar quantos valores: ')
                            amount = func.checknumeric(nm)
                    break
                else:
                    clear()
                    func.title('DELETANDO DADOS')
                    print('[red]:X: Por favor, digite apenas números[/]')
                    nm = input('Deseja apagar quantos valores: ')
                    amount = func.checknumeric(nm)
        break
    else:
        print('[red]:X: Digite um número válido![/]')
        opc = input('Digite sua opção: ')
# FECHANDO O BANCO DE DADOS
dao.close()
