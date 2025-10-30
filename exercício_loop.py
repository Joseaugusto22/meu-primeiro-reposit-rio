#exercício 01
frutas = ["maça","banana","laranja","uva"]
#exercício 02
frutas[0]
frutas[-1]
#exercício 03 
frutas.append ("manga")
#exercício 04
frutas.remove ("banana")
#exercício 05
indice = frutas.index("laranja")
frutas[indice]= "abacaxi"
#exercício 06
numeros = list(range(1,11))
#exercício 07
soma = sum(numeros)
print(soma)
#exercício 08
max(numeros)
min(numeros)
#exercício 09
list(reversed(numeros))
#exercício 10
cidades = ["são paulo", "rio de janeiro", "belo horizonte","cuiabá"]
#exercício 11
sorted(cidades)
#rxercício 12
cidades.append("Porto Alegre")
print(cidades)
#exercício 13
cidades.index("cuiabá")
#exercício 14
cidades.remove("rio de janeiro")
#exercíco 15
lista1 = list(range(1,4))
lista2 = list(range(4,7))
#exercício 16
lista3= lista1 + lista2
print(lista3)
#exercício 17
print (lista3)
#exercício 18
lista_domésticos = ["cachorro", "gato", "coelho"] 
lista_selvagens = ["leão", "tigre", "urso"]
#exercício 19
lista_todos_animais = lista_domésticos + lista_selvagens
print(lista_todos_animais)
#exercício 20
print (lista_todos_animais)   
#exercício 21
nomes = ["Ana", "Pedro", "Maria", "João"]
#Exercício 22
for nome in nomes:
    print(nome.upper())
#exercício 23
nomesmaiusculos = []
for nome in nomes:
    nomesmaiusculos.append(nome.upper())
print(nomesmaiusculos)
#exercício 24

for numero in (range(1, 21)):
  
  if numero % 2 == 0:
    print(numero)

#exercício 25
for numero in range(1,21):
   print(numero**2)

#exercício 26
programas = ["java","python","c","javascript"]
for programa in programas:
   print(f"o programa '{programa}' tem {len(programa)} letras.")

#exercício 27
idades = [12, 18, 25, 40, 60]
for idade in idades:
  if idade >= 18:
    print(f"{idade}: maior de idade")
  else:
    print(f"{idade}: menor de idade")
  
  #exercício 28
notas = [5.5, 7.0, 8.3, 4.9, 6.2]
aprovados = 0
reprovados = 0
for nota in notas:
  if nota >= 7.0:
    
    aprovados += 1  
  else:
    reprovados += 1 
print(f"Total de alunos aprovados: {aprovados}")
print(f"Total de alunos reprovados: {reprovados}")

#exercício 29
palavras = ["arara", "banana", "radar", "python"]
for palavra in palavras:
   if palavra==palavra[::-1]:
    print(palavra)
    
# ex 31
print(" Exercício 31: Números de 1 a 10 ")
contador = 1
while contador <= 10:
    print(contador)
    contador += 1


# ex 32
print("Exercício 32: Entrada até digitar 0 ")
numero = -1
while numero != 0:
    try:
        entrada = input("Digite um número inteiro (0 para sair): ")
        numero = int(entrada)
        if numero != 0:
            print(f"Você digitou: {numero}")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")


# ex 33
print(" Exercício 33: Soma de 1 a 100 ")
soma = 0
numero = 1
while numero <= 100:
    soma += numero
    numero += 1
print(f"A soma dos números de 1 a 100 é: {soma}")


#ex 34
print(" Exercício 34: Jogo de Adivinhação ")
numero_secreto = 7
palpite = 0

while palpite != numero_secreto:
    try:
        entrada_palpite = input("Adivinhe o número secreto (entre 1 e 10): ")
        palpite = int(entrada_palpite)
        if palpite != numero_secreto:
            print("Errado. Tente novamente!")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print("Parabéns! Você acertou o número secreto!")


# ex 35
print(" Exercício 35: Pares de 2 a 20 ")
numero = 2
while numero <= 20:
    print(numero)
    numero += 2
