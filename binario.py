
import emoji

valor = input('Insira um valor a ser criptografado: ')
for c in valor:
    v = ord(c)
    print(c, v, f'{v:b}', sep='\t')