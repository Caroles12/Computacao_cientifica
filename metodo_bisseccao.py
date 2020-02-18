#importar a biblioteca matematica

import math

#Definir o intervalo e o erro de parada
a = 2
b = 3
e = 0.05

#Definir uma função no python
def f(x):
   #escrevendo a função
    return x**3 -9*x + 3

#Verificação do intervalo da função
if f(a)*f(b) < 0:
   #Quando o modulo de b-a/2 for maior que o erro, executa o laço
   while(math.fabs(b-a)/2 > e):
       xi = (a+b)/2
       if f(xi)==0:
           print("A raiz é: " ,xi)
           break
       else:
            if f(a)*f(xi) < 0:
                b = xi
            else:
                a = xi

   print("O valor da raiz é:" ,xi)


else:
    print("Não há raiz no intervalo")