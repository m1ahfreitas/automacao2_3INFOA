'''
As funções permitem modularizar o código, dividir ele em partes menores que podem ser reaproveitadas, isso simplifica a codificação.

Estrutura função em phyton

def nome_funcao(param1, param2, paramN):
    //algum código que a função faz
    return valor_retornado

'''

## criar uma função que calcula a área do triãngulo
def calculateTriangleArea(base, altura):
   area = (base*altura) / 2
   return area

## criar uma função que calcula a área do triãngulo
def calculateSquareArea(lado):
   area = lado * lado
   return area

'''
#Exemplo 1: chamar a função
area1 = calculateTriangleArea(100,10)
print("A área do triãngulo 1 é ", area1)

#Exemplo 2 : Chamar a função novamente 
base = float(input('Digite a base: '))
altura = float(input('Digite a altura:'))
area2 = calculateTriangleArea(base, altura)
print("A area do Triangulo é", area2)
'''