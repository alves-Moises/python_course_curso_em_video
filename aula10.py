tempo = int(input("quantos anos tem seu carro?"))
if tempo>=3:
    print('carro velho')
else:
    print('carro novo')

nome = str(input("say your name: "))
if nome == 'abc':
    print('true')
else:
    print('false')

n1 = float(input('Note 1: '))
n2 = float(input('Note 2: '))
print(f'Media: {(n1+n2)/2:.2f}')
m = (n1+n2)/2
if m >=6:
    print('Apvoved')
else:
    print('reproved')