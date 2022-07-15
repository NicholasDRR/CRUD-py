from rich import print
# Printando alguns -
def less():
    print('[red]-[/]' * 24)


# Checando se o nome é apenas string.
def checkstr(name):
    return name.isalpha()



# Convertendo float pra string
def convert(price):
    tprice = str(price).replace('.', '')
    return tprice


# Checando se o preço são números.
def checknumeric(price):
    return price.isnumeric()

# Mostra o título
def title(ttl):
    less()
    print(f'{ttl}'.center(24))
    less()