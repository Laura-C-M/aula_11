import math
print("Esta é uma calculadora simples diz-me o valor e a operação que queres fazer e eu faço-a!")
n1 = float(input("Escolhe um valor"))
op = str(input("Qual a operação que queres fazer? Soma(+), subtração(-), multiplicação(*), divisão(/), raiz quadrada(r), quadrado (q)"))
if op != "r":
 n2 = float(input("Escolhe outro valor"))
if op == "+" :
    print("A soma de ", n1 ," com " , n2 , "é igual a" , n1+n2)
elif op == "-" :
    print("A subtração de ", n1 ," com " , n2 , "é igual a" , n1-n2)
elif op == "*" :
    print("A multiplicação de ", n1 ," com " , n2 , "é igual a" , n1*n2)
elif op == "/":
    print("A divisão de ", n1, " com ", n2, "é igual a", n1/n2)
elif op == "r":
    print("A raíz quadrada de" , n1, "é igual a ", math.sqrt(n1))
elif op == "q":
    print("A potência de" , n1,"elevado a", n2 ,"é igual a ", n1**n2)

#def operação(op):

