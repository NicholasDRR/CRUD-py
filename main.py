from CRUD.validate import dao, func
from rich import print
from rich.table import Table
import os
clear = lambda : os.system('cls')
# teste
# import os
# print("\n" * os.get_terminal_size().lines)
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
            func.less()
            print('INSERINDO DADOS'.center(24))
            func.less()
            name = input('Nome: ')
            name_product = func.checkstr(name)
            while True:
                if name_product:
                    break
                else:
                    print('[red]Por favor, digite apenas letras[/]')
                    name = input('Nome: ')
                    name_product = func.checkstr(name)
            number = input('Preço: ')
            price = func.checknumeric(func.convert(number))
            while True:
                if price:
                    break
                else:
                    print('[red]Por favor, digite apenas números[/]')
                    number = input('Preço: ')
                    price = func.checknumeric(func.convert(number))
            if name_product and price:
                try:
                    dao.insert(name, number)
                    print('[green]:heavy_check_mark: Produto adicionado[/]')
                except:
                    print('[red]ERRO! (desconhecido)[/]')
        # READ
        if opc == '2':
            tbl = input('Qual tabela deseja ver: ')
            table = func.checkstr(tbl)
            while True:
                if table:
                    try:
                        read = dao.read(tbl)
                        table = Table(title='[yellow]DADOS DA TABELA[/]', style='yellow')
                        table.add_column('Id_product')
                        table.add_column('Name_product')
                        table.add_column('Price')
                        for i in read:
                            table.add_row(str(i[0]), str(i[1]), str(i[2]))
                        print(table)
                        break
                    except:
                        print('[red]ERRO! (tabela desconhecida).[/]')
                        tbl = input('Qual tabela deseja ver: ')
                        table = func.checkstr(tbl)

                else:
                    print('[red]Digite apenas letras.[/]')
                    tbl = input('Qual tabela deseja ver: ')
                    table = func.checkstr(tbl)
        # UPDATE
        if opc == '3':
            func.less()
            print('ATUALIZANDO VALORES'.center(24))
            func.less()
            print('''1: Nome
2: Preço''')
            func.less()
            att = input('Atualizar: ')
            while True:
                if att == '1':
                    nwname = input('Novo nome: ')
                    new_name = func.checkstr(nwname)
                    while True:
                        if new_name:
                            break
                        else:
                            print('[red]Digite apenas letras.[/]')
                            nwname = input('Novo nome: ')
                            new_name = func.checkstr(nwname)
                    idp = input('Id do produto: ')
                    id_product = func.checknumeric(idp)
                    while True:
                        if id_product:
                            break
                        else:
                            print('[red]Digite apenas números.[/]')
                            id_product = func.checknumeric(input('Id do produto: '))
                    if new_name and id_product:
                        try:
                            dao.update(nwname, idp)
                            print('[green]:heavy_check_mark: Nome atualizado![/]')
                        except:
                            print('[red]ERRO (desconhecido)[/]')
                    break
                elif att == '2':
                    np = input('Novo preço: ')
                    new_price = func.checknumeric(func.convert(np))
                    while True:
                        if new_price:
                            break
                        else:
                            print('[red]Digite apenas números[/]')
                            np = input('Novo Preço: ')
                            new_price = func.checknumeric(func.convert(np))
                    idp = input('Id do produto: ')
                    id_product = func.checknumeric(idp)
                    while True:
                        if id_product:
                            break
                        else:
                            print('[red]Digite apenas números.[/]')
                            idp = input('Id do produto: ')
                            id_product = func.checknumeric(idp)
                    if new_price and id_product:
                        try:
                            dao.update(np, idp)
                            print('[green]:heavy_check_mark: Preço atualizado[/]! ')
                        except:
                            print('[red]ERRO (desconhecido)[/]')
                    break
                else:
                    print('[red]Escolha entre [blue]1[/] e [blue]2[/][/]')
                    att = input('Atualizar: ')
                # DELETE
        # DELETE
        if opc == '4':
            nm = input('Deseja apagar quantos valores: ')
            amount = func.checknumeric(nm)
            while True:
                if amount:
                    while True:
                        if nm == '1':
                            id = input('Id do produto: ')
                            id_product = func.checknumeric(id)
                            while True:
                                if id_product:
                                    try:
                                        dao.delete(id)
                                        print(f'[green]:heavy_check_mark: Produto com id: {id} deletado![/]')
                                        break
                                    except:
                                        print('[red]ERRO! Digite um id válido.[/]')
                                else:
                                    print('[red]Digite apenas números.[/]')
                                    id = input('Id do produto: ')
                                    id_product = func.checknumeric(id)
                            break
                        elif int(nm) > 1:
                            id_product = []
                            for c in range(int(nm)):
                                while True:
                                    np = input(f'{c + 1}º id: ')
                                    number = func.checknumeric(np)
                                    if number:
                                        id_product.append(np)
                                        for ids in id_product:
                                            dao.delete(ids)
                                        print(f'[green]:heavy_check_mark: Id {np} deletado![/]')
                                        break
                                    else:
                                        print('[red]Digite um id válido[/]')
                            break
                        else:
                            print('[red]Número inválido[/]')
                            nm = input('Deseja apagar quantos valores: ')
                            amount = func.checknumeric(nm)
                    break
                else:
                    print('[red]Por favor, digite apenas números[/]')
                    nm = input('Deseja apagar quantos valores: ')
                    amount = func.checknumeric(nm)

        break
    else:
        print('[red]Digite um número válido![/]')
        opc = input('Digite sua opção: ')