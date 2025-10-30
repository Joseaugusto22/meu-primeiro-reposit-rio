nome = "Jose" 
idade = 18
altura = 1.78
estudante = "sim"
print(nome)
type(idade)
type(nome)

#exercício 2

idade = input("digite sua idade")
idade = int (idade) + 5
print (f"sua idade em 5 anos será {idade}")

#Exercício 3 

num1 = input("digite o número 1")
num2 = input("digite o número 2")
num1 = int(num1)
num2 = int(num2)
soma = num1 + num2
print(f"Sua idade somada é {soma}")

#exercício 4
num3 = int(input("digite o primeiro número"))
num4 = int(input("digite o segundo número"))           
média = (num3 + num4)/2
print(f"sua média é: {média}")

#exercício 5 
nota1 = int(input("digite sua nota 1"))
nota2 = int(input("digite sua nota 2"))         
nota3 = int(input("digite sua nota 3"))               
notafinal = (0.2 * nota1) + (0.4 * nota2) + (0.4 * nota3)
print(f"sua nota final é: {notafinal}")

#exercício 6
nomecompleto = str(input("digite seu nome completo"))
print(nomecompleto.split()[0])
print(len(nomecompleto))
