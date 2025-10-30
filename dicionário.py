# Questão 01 

aluno = {
    "nome": "Jose",
    "idade": 18,
    "curso": "Economia"
}

print(f"Nome: {aluno["nome"]}\nIdade: {aluno["idade"]}\nCurso: {aluno["curso"]}")


# Questão 02 

produto = {
    "nome": "Teclado Mecânico",
    "preco": 350.00,
    "estoque": 10
}
produto["marca"] = "hyperx"
produto["preco"] = 320.00
produto["estoque"] = 8
del produto["marca"]
print(produto)


# Questão 03
notas = {
    "Alice": 8.5,
    "Bruno": 7.0,
    "Carla": 9.2,
    "Daniel": 6.8
}

for aluno, nota in notas.items():
    print(f"{aluno}: {nota}")

media = round(sum(notas.values())/len(notas), 2)
print(f"A média é {media}")


# Questão 04

numeros = {"a": 47, "b":78, "c": 14}
soma = sum(numeros.values())
print(f"A soma dos números é {soma}")


# Questão 05 

lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
dicionario = {"maçã":0,"banana":0,"laranja":0}
for repetidos in lista:
    if repetidos=="maçã":
        dicionario["maçã"] = dicionario["maçã"]+1
    elif repetidos=="banana":
        dicionario["banana"] = dicionario["banana"]+1
    elif repetidos=="laranja":
        dicionario["laranja"] = dicionario["laranja"]+1


# Questão 06 

produtos = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}
produtos_50 = {}

for produto, valor in produtos.items():
    if valor<=50:
        produtos_50[produto] = valor

print(produtos_50)


# Questão 07 

tradutor = {
    "Hello": "Olá",
    "Food": "Comida",
    "Restroom": "Banheiro",
    "Order": "Pedido"
    }

palavra = input("Digite uma palavra em inglês: ")
traducao = tradutor.get(palavra)

if traducao:
    print(f"A tradução de {palavra} é {traducao}")
else:
    print("Palavra não encontrada")


# Questão 08 
compras = {}
funcao = input("Você quer remover ou adicionar itens na lista?")

if funcao=="Remover" or funcao=="remover":
    item = input("Qual item você quer remover?")
    if item in compras:
        compras.pop(item)
        print(f"{item} foi removido(a) da lista de compras")
        print(f"Lista atualizada: {compras}")
    else:
        print(f"{item} não está na lista")

elif funcao=="Adicionar" or funcao=="adicionar":
    item = input("Qual item você quer adicionar?")
    quant = int(input("Qual a quantidade desse item?"))
    if item in compras:
        compras[item] = compras[item] + quant
    else:
        compras[item] = quant
    print(f"A lista foi atualizada: {compras}")

else:
    print("Falha! Escreva apenas 'remover' ou 'adicionar'")


# Questão 09 

turma = {
    "Ana": {"idade": 17, "notas": [8, 9, 7]},
    "Pedro": {"idade": 18, "notas": [6, 7, 8]},
    "Mariana": {"idade": 17, "notas": [9, 10, 8]},
}

turma["João"] = {"idade": 19, "notas": [8, 4, 6]}

print("Médias:")
for nome, info in turma.items():
    notas = info["notas"]
    media = sum(notas)/len(notas)
    print(f"{nome}: {media}")


# Questão 10 

funcionarios = {}

opcao = input("Você quer adicionar um funcionário novo ou consultar os funcionários existentes?")

if opcao=="adicionar" or opcao=="Adicionar":
    nome = input("Digite o nome do funcionário")
    cargo = input("Digite o cargo do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    funcionarios[nome] = {"cargo": cargo, "salario": salario}
    print("Funcionário cadastrado")
    print(funcionarios[nome])

elif opcao=="Consultar" or opcao=="consultar":
    nome = input("Digite o nome do funcionário: ")
    cargo = (funcionarios[nome])["cargo"]
    salario = (funcionarios[nome])["salario"]
    print(f"Nome: {nome}\nCargo: {cargo}\nSalário: {salario}")
