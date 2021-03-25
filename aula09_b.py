#========AULA 9 TESTES
frase1 = input('Type what do you wanna: ')
#frase1.replace('OLA','ANDRO')
#frase1[4]
#frase1[4::3]
#frase1[4:20]
#frase1[4:20:2]
#frase1.upper() #maiusculo
#frase1.lower() #minusculo
#frase1.capitalize() #primeira letra em maiusulo
#frase1.title() #iniciais de palavras em maiusculo
#frase1.strip() #reoção de espaços inadequados
#frase1.split() #separação de palavras
#'-'.join(frase1)
#frase1.count(' ')

print('phrase\'s len: ', len(frase1))
print(f'Lettlers: \'a\' in the phrase:', frase1.lower().count('a'))
print(f'Were\'s \'a\' in the phrase:', frase1.lower().find('a'))
print('Have \'abc\' in the phrase? ', ('abc' in frase1))
print(frase1.replace('abc', 'substuited'))
print(frase1.upper(), frase1.lower())
print(frase1.capitalize())
print(frase1.title())
print('Espaces removed from out: ', frase1.strip()) #corta os espaços ao redor da string
print('Espaces removed from right out: ', frase1.rstrip())
print('Espaces removed from left out: ', frase1.lstrip())
print(frase1.split())
print('=.='.join(frase1))
#frase = ('')
#print(frase1.find(''))