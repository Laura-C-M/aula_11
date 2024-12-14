frase = str(input("Escreve uma frase"))
letra = str(input("Escolhe uma letra e vou dizer-te quantas vezes esta aprarece na frase"))
n = frase.count(letra)
print("A letra", letra, "aparece", n, "vezes na frase")