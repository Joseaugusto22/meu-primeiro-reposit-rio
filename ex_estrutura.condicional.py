  #exercício 1
#Leia um número inteira e informe se é par ou ímpar
num1 = int(input("digite o número")) 
if num1 % 2 == 0: 
    print("o número é par")
else:
    print("o número é ímpar")

  #exercício 2
#Aprovado ou Reprovado
nota = float(input("digite a sua nota"))
if nota >= 7: 
 print("aprovado")
else:
 print("reprovado")

   #exercício 3
valorconta = float(input("digite o valor da compra"))
if valorconta > 100:
   desconto = valorconta * 0.1
   preçofinal = valorconta - desconto
   print(f"sua compra ficou nop valor de {preçofinal}")
else: 
   preçofinal = valorconta
   print(f"sua compra ficou no valor de {preçofinal}")

   #exercício 4 
temperatura = float(input("digite a temperatura em Celsius"))
converter_fahrenheint = float(temperatura * 1.8) + 32
print(f"a temperatura é {converter_fahrenheint}")

  #exercício 5
numero1 = int(input("digite o primeiro número"))
numero2 = int(input("digite o número 2"))
if numero1 > numero2:
 print("o primeiro número é maior ")
else:
  print("o segundo número é maior")
if numero1 == numero2:
    print("os números são iguais")

 #exercício 6
firstnumber = int(input("digite o primeiro número"))
secondnumber = int(input("digite o segunda número"))
thirdnumber = int(input("digite o terceiro número"))
maior = firstnumber
if maior < secondnumber:
   maior = secondnumber
if maior < thirdnumber:
    maior = thirdnumber
print(f"o maior número é {maior}")

#exercício 7
n1 = float(input("digite o primeiro número"))
n2 = float(input("digite o segunda número"))
operação = (input("digite o sinal da operação"))
if operação == "+":
   resultado = n1 + n2
elif operação == "-":
   resultado = n1 - n2
elif operação == "/":
    if n2 != 0:
      resultado = n1 / n2
    else:
      print("divisão por zero")
elif operação== "*":
    resultado = n1 * n2 
print(resultado)

#exercício 8
entrada = input("Digite os números separados por espaço: ")
numeros = [int(n) for n in entrada.split()]

positivos = 0
negativos = 0
zeros = 0

for n in numeros:
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
    else:
        zeros += 1
print(positivos, "positivos,", negativos, "negativos,", zeros, "zeros")


#exercício 9
ano = int(input("digite o ano"))
if ano % 4 == 0:
   print("ano bissexto")
else:
   print("não bissexto")

   #exercício 10
idade = int(input("digite a idade")) 
if idade >= 18 and idade <= 65:
   print("idade aprovada") 
else:
   print("idadade não aprovada")

#exercício 11

user=input("digite o usuário")
password=input("digite a senha")
if user=="jose" and password=="1234":
    print ("liberado")
else:
    print("negado")

    #Exercício 12

    sua_idade = int(input("digite a idade")) 
    if sua_idade < 16:
       print("não vota")
    if sua_idade >= 18 and sua_idade <= 70:
       print("voto obrigatório")
    if sua_idade > 70:
       print ("voto facultativo")

#exercício 13

seu_numero = int(input("digite o numero")) 
if seu_numero >= 10 and seu_numero <= 50:
   print ("está dentro do intervalo")
else:
   print("não está dentro do intervalo")

   #exercício 14
   sua_nota = float(input("digite a sua nota final"))
   if sua_nota >= 7:
      print("aprovado")
if sua_nota >= 5 and sua_nota < 7:
      print("recuperação")

if sua_nota < 5:
    print("reprovado")