import emoji
from math import sqrt, floor, ceil
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} equivale a: {}.'.format(num, floor(raiz)))
print('A raiz quadrada de {} equivale a: {}.'.format(num, ceil(raiz)))
print(emoji.emojize('Tá vendo :earth_americas:', use_aliases=True))
print(emoji.emojize('Mito :sunglasses:', use_aliases=True))

