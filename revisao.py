#Variáveis
#exercício 01
nome = "José"
idade = 18
altura = 1.78
estudante = "sim"
type(nome)
type(idade)  
type(altura)

#Exercício 02
idade = input("digite sua idade")
idade = int(idade) + 5
print (f"sua idade em 5 anos será {idade}")

#exercício 03
numero1 = input("digite o número")
numero2 = input("digite o número")
numero1 = int(numero1) 
numero2 = int(numero2)      
resultado = numero2 + numero1
print(resultado)

#exrcício 04
n1 = input("digite o número")
n2 = input("digite o número")
n3 = input("digite o número")
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
media = (n1 + n2 + n3) /  3
print(f"sua media é {media}")    

#exercício 05
ap1 = float(input("digite sua nota "))
ap2 = float(input("digite sua nota ")) 
ac = float(input("digite sua nota "))
nota_final = ap1 * 0.4 + ap2 * 0.4 + ac * 0.2
print(f"sua nota final é {nota_final}") 

#exercício 06
nome = input("digite seu nome")
nome_maiusculo = nome.upper()
print(nome_maiusculo)   
primeiro_nome = nome.split()
print(primeiro_nome)    
numero_letras = len(nome)  
print(numero_letras -1 )


#Exercícios CONDICIONAIS
#exercício 01
n = int(input("digite seu número"))
if n % 2 == 0:
    print("par")
else:
    print("impar")

#exercício 02 
nota = float(input("digite sua nota"))
if nota >= 7:
    print("aprovado")
else:
    print("reprovado")

#exercício 03 
valor_compra = float(input("digite o valor da compra"))
desconto = valor_compra * 0.9
if valor_compra >= 100:
    print(desconto)
else:
    print(valor_compra)

#exercício 04 
celsius = float(input("digite a temperatura em celsius"))
Far = celsius * 9/5 + 32
print (Far)

#exercício 05 
first_number = int(input("type first number"))
second_number = int(input("type second number"))
if first_number > second_number:
    print("first number is bigger then second")
elif first_number == second_number:
    print("same number")
else:
    print("second number is bigger then first")

#exercício 06
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
maior_numero = max(num1, num2, num3)
print(maior_numero)

#exercicio 10
age = int(input("digite sua idade"))
if 18 <= age <= 65:
    print("permitido")
else:
    print("n permitido")

#exercício 11
senha = int(input("digite a senha"))
senha_correta = 1234
if senha == senha_correta:
    print("senha correta")
else:
    print("tente novamente")

    #exercício 12
sua_idade = int(input("digite sua idade"))
if sua_idade < 16:
    print("não vota")
elif 18 <= sua_idade <= 70:
    print("voto obrigatório")
elif sua_idade > 70 or 16 <= sua_idade < 18:
    print("voto facultativo")

#exercício 14
sua_nota = float(input("digite sua nota"))
if sua_nota >= 7:
    print("aprovado")
elif 5 <= sua_nota < 7:
    print("recuperação")
else:
    print("reprovado")

#EXERCÍCIOS DE LISTA
frutas = ["maçã","banana","uva","laranja"]
print(frutas[0])
frutas[-1]
frutas.append("manga")
print(frutas)
frutas.remove("manga")
print(frutas)
frutas.remove("banana")
frutas[0] = "abacaxi"
numeros = list(range(1,11))
sum(numeros)
max(numeros)
min(numeros)
sorted(frutas)

cidades = ["são paulo","goiânia", "paulo afonso","petrolina"]
sorted(cidades)
cidades.append("porto alegre")
print(cidades)

idades = [14,18,28,17]
for idade in idades:
    if idade >= 18:
        print(f"a idade {idade} é de maior")

notas = [5.5, 7.0, 8.3, 4.9, 6.2]
for nota in notas:
    if nota >= 6:
        print(f"a nota {nota} passa de ano")
        

contador = 1
while contador <= 10:
    print(contador)
    contador = contador + 1  

soma = 0
numero_atual = 1
while numero_atual <= 100:
    soma = soma + numero_atual  
    numero_atual = numero_atual + 1  
print(f"A soma dos números de 1 a 100 é: {soma}")


nomes = ["jose","joão","pedro","felipe"]
nomes[0]
nomes[-1]

lista = list(range(1,101))
lista[50]

#Aprendendo DICIONÁRIO
#criando meu primeiro dicionário

alunos = {
    "nome": "Jose",
    "idade": 18,
    "curso": "economia"
}
print(alunos)
#adicionando itens
alunos["altura"] = 1.78
print(alunos) 

#resolvendo exercícios 
#construindo o dicionário
produto = {
    "nome":"teclado",
    "preço": 350,
    "estoque": 10
}
#adicionando elementos 
produto["marca"] = "hyperX"
produto["estoque"] = 8
print(produto)
produto["estoque"]

#Removendo chaves
del produto["marca"]

#criando outro dicionário
notas = {
    "Alice": 8.5,
    "Bruno": 7.0,
    "Carla": 9.2,
    "Daniel": 6.8
}
print(notas)

#Fazendo a média das notas da lista
Notas_da_lista = notas.values()
Soma_das_notas = sum(Notas_da_lista)
Numero_de_alunos = len(notas)
Média = Soma_das_notas / Numero_de_alunos
print(f"a média das notas dos alunos é {Média}")


numeros = {"a": 10, "b": 20, "c": 30}
contando_os_valores = numeros.values()
soma_dos_numeros = sum(contando_os_valores)
print(f"a soma dos números é {soma_dos_numeros}")

#lista em dicionário
lista_frutas = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
frequncia = {}
for fruta in lista_frutas:
    if fruta in frequncia:
        frequncia[fruta] = frequncia[fruta]+1
    else:
         frequncia[fruta] = 1
         print(frequncia)   
        

        



pele = input("branco,preto,pardo,amarelo")
escola = input("particular ou pública")
if escola == "pública" and pele == "preto" or "pardo" or "amarelo":
    print("você tem direito as cotas")
else:
    print("voce não tem direito as cotas")

meu_dicionário = {
    "nome":"josé",
    "idade": 18,
    "altura": 1.78,
}
print(meu_dicionário)
meu_dicionário["perna dominante"] = "direito"
print(meu_dicionário)


#exercício 04

from collections import Counter
lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
frequencia = Counter(lista)
print(frequencia)

print(dict(frequencia))


tintas = {
 "azul": 100,
 "branco" : 160,
 "preto" : 140,
 "verde" : 90

}
itens_caros = {}
for produto, preço in tintas.items():
    if preço > 100:
        itens_caros[produto] = preço
print(itens_caros)


tradutor = {
    "hello": "olá",
    "world": "mundo",
    "cat": "gato",
    "dog": "cachorro",
    "book": "livro",
    "python": "python" 
}
palavra_ingles = input("Digite uma palavra em inglês para traduzir: ")
if palavra_ingles in tradutor:
    
    traducao = tradutor[palavra_ingles]
    print(f"A tradução é: {traducao}")
else:
    # Se não existir, exibe a mensagem de erro.
    print("Palavra não encontrada.")


    turma = {
    "Ana": {"idade": 17, "notas": [8, 9, 7]},
    "Pedro": {"idade": 18, "notas": [6, 7, 8]},
    "Mariana": {"idade": 17, "notas": [9, 10, 8]}
}
turma["josé"] = {"idade" : 18, "notas": [8,9,10]}
print(turma)

soma_total_notas = sum(nota for dados in turma.values() for nota in dados["notas"])

print(soma_total_notas)













turma = {
    "Ana": {"idade": 17, "notas": [8, 9, 7]},
    "Pedro": {"idade": 18, "notas": [6, 7, 8]},
    "Mariana": {"idade": 17, "notas": [9, 10, 8]}
}
turma["José"] = {"idade" : 18, "notas": [8,9,10]}
print(turma)

somando_as_notas = 0

for aluno, dados in turma.items():
    notas_dos_alunos = dados["notas"]
    soma_Das_notas = sum(notas_dos_alunos)
    somando_as_notas += soma_Das_notas

print(f"A soma total e final das notas é: {somando_as_notas}")
    



faturamento = [
    {"dia": "segunda", "valor": 1200},
    {"dia": "terça", "valor": 1500},
    {"dia": "quarta", "valor": 900},
    {"dia": "quinta", "valor": 1800},
    {"dia": "sexta", "valor": 2400},
]


faturamento = [
    {"dia": "segunda", "valor": 1200},
    {"dia": "terça", "valor": 1500},
    {"dia": "quarta", "valor": 900},
    {"dia": "quinta", "valor": 1800},
    {"dia": "sexta", "valor": 2400},
]

faturamento_total = sum(registro["valor"] for registro in faturamento)

print(f"O faturamento total do período foi de: R$ {faturamento_total:.2f}")




compras = [
 {"cliente": "Maria", "valor": 450},
 {"cliente": "José", "valor": 1200},
 {"cliente": "Clara", "valor": 3000},
]
valores = [450,1200,3000]
for valor in valores:
    if valor < 500:
        print(valor*0.95)
    elif 500 <= valor < 2000:
        print (valor * 0.9)
    elif valor >= 2000:
        print(valor * 0.85)

avaliacao = {
    "ana" : 9,
    "carlos" : 6,
    "joao" : 7
}
for nome, nota in avaliacao.items():
    if nota >= 9:
        print(f"{nome}:excelente")
    elif 7 <= nota <= 8.9:
        print(f"{nome}: bom")
    else:
        print(f"{nome} :estudar mais")        



avaliacao = {
    "ana": 9,
    "carlos": 6,
    "joao": 7
}

for nome, nota in avaliacao.items():
    if nota >= 9:
        # Usando f-string para incluir a variável 'nome'
        print(f"{nome}: excelente")
    elif 7 <= nota <= 8.9:
        # Usando f-string aqui também
        print(f"{nome}: bom")
    else:
        # E aqui
        print(f"{nome}: estudar mais")



        faturamento = [
    {"dia": "segunda", "valor": 1200},
    {"dia": "terça", "valor": 1500},
    {"dia": "quarta", "valor": 900},
    {"dia": "quinta", "valor": 1800},
    {"dia": "sexta", "valor": 2400},
]

soma_salario = max(registro["valor"] for registro in faturamento)
print(soma_salario)   