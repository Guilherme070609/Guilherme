#Crie duas variaveis e atribua velores internos
#divida a maior pela menor e virifique se o resto da divisão deu zero. Se deu zero 
#imprima "O numero maior é impar". Use divisão //, para o resto use %

var1 = 12
var2 = 2

if var1 > var2:
    modulo = var1 % var2
else:
    modulo = var2 % var1

if modulo == 0:
    print("o numero maior é par")
else:
    print("o numero maior é impar")
