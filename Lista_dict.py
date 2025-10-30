faturamento = [
    {"dia": "segunda", "valor": 1200},
    {"dia": "terça", "valor": 1500},
    {"dia": "quarta", "valor": 900},
    {"dia": "quinta", "valor": 1800},
    {"dia": "sexta", "valor": 2400},
]

faturamento_total = 0
for venda in faturamento:
    faturamento_total += venda["valor"]
print(faturamento_total)

maior_valor = 0
dia_maior_faturamento = ""
for venda in faturamento:
    if venda["valor"] > maior_valor:
        maior_valor = venda["valor"]
        dia_maior_faturamento = venda["dia"]
print(dia_maior_faturamento)

media_vendas = faturamento_total / len(faturamento)
print(media_vendas)

estoque = {
    "notebook": [5, 7, 3],
    "mouse": [20, 25, 18],
    "teclado": [12, 14, 9],
}
totais_por_produto = {}
menor_estoque = -1
produto_menor_estoque = ""

for produto, estoques_filiais in estoque.items():
    total_produto = 0
    for quantidade in estoques_filiais:
        total_produto += quantidade
    
    totais_por_produto[produto] = total_produto
    print(f"{produto}: {total_produto} unidades")

for produto, total in totais_por_produto.items():
    if menor_estoque == -1 or total < menor_estoque:
        menor_estoque = total
        produto_menor_estoque = produto
print(produto_menor_estoque)

print(totais_por_produto)

funcionarios = [
    {"nome": "Ana", "salario": 4500, "departamento": "RH"},
    {"nome": "Carlos", "salario": 7000, "departamento": "TI"},
    {"nome": "Beatriz", "salario": 5200, "departamento": "Financeiro"},
    {"nome": "João", "salario": 4800, "departamento": "TI"},
]

folha_salarial_total = 0
for func in funcionarios:
    folha_salarial_total += func["salario"]
print(folha_salarial_total)

maior_salario = 0
nome_mais_bem_pago = ""
for func in funcionarios:
    if func["salario"] > maior_salario:
        maior_salario = func["salario"]
        nome_mais_bem_pago = func["nome"]
print(nome_mais_bem_pago)

salarios_por_departamento = {}
for func in funcionarios:
    departamento = func["departamento"]
    salario = func["salario"]
    if departamento not in salarios_por_departamento:
        salarios_por_departamento[departamento] = 0
    salarios_por_departamento[departamento] += salario
print(salarios_por_departamento)

numeros = {"a": 10, "b": 20, "c": 30, "d": 5}
soma_total = 0
for chave in numeros:
    soma_total += numeros[chave]
print(soma_total)

lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
frequencia = {}
for item in lista:
    if item in frequencia:
        frequencia[item] += 1
    else:
        frequencia[item] = 1
print(frequencia)

produtos = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}
produtos_caros = {}
valor_minimo = 50
for produto, preco in produtos.items():
    if preco > valor_minimo:
        produtos_caros[produto] = preco
print(produtos_caros)

tradutor = {
    "hello": "olá",
    "dog": "cachorro",
    "cat": "gato",
    "house": "casa"
}

palavra_ingles = input("Digite uma palavra em inglês para traduzir (ex: 'dog'): ").lower()

if palavra_ingles in tradutor:
    traducao = tradutor[palavra_ingles]
    print(traducao)
else:
    print("Palavra não encontrada")

estoque_alerta = {
    "notebook": 3,
    "mouse": 25,
    "teclado": 8,
    "monitor": 2
}
for produto, quantidade in estoque_alerta.items():
    mensagem = ""
    if quantidade < 5:
        mensagem = "Estoque crítico"
    elif quantidade <= 10:
        mensagem = "Estoque baixo"
    else:
        mensagem = "Estoque adequado"
    print(f"{produto}: {quantidade} - {mensagem}")

vendas_regiao = [
    {"regiao": "Sul", "valor": 12000},
    {"regiao": "Norte", "valor": 8000},
    {"regiao": "Sudeste", "valor": 20000},
    {"regiao": "Centro-Oeste", "valor": 5000},
]
meta = 10000
lista_situacao = []

for venda in vendas_regiao:
    regiao = venda["regiao"]
    valor = venda["valor"]
    situacao = ""
    
    if valor >= meta:
        situacao = "Meta atingida"
    else:
        situacao = "Meta não atingida"
    
    print(f"{regiao}: R$ {valor:.2f} -> {situacao}")
    
    nova_venda = {"regiao": regiao, "situacao": situacao}
    lista_situacao.append(nova_venda)

print(lista_situacao)

cadastro_funcionarios = {}

def adicionar_funcionario_simples():
    nome = input("Digite o NOME do funcionário para cadastrar: ")
    cargo = input("Digite o CARGO: ")
    salario = input("Digite o SALÁRIO: ")
    
    dados_funcionario = {
        "Cargo": cargo,
        "Salário": salario
    }
    cadastro_funcionarios[nome] = dados_funcionario
    print(f"Funcionário {nome} cadastrado com sucesso!")

def consultar_funcionario_simples():
    nome_consulta = input("Digite o NOME do funcionário para consultar: ")
    
    if nome_consulta in cadastro_funcionarios:
        dados = cadastro_funcionarios[nome_consulta]
        print(f"Detalhes de {nome_consulta}:")
        print(f"  Cargo: {dados['Cargo']}")
        print(f"  Salário: R$ {dados['Salário']}")
    else:
        print(f"Funcionário '{nome_consulta}' não encontrado.")

while True:
    print("--- Menu Cadastro/Consulta ---")
    print("1. Adicionar Funcionário")
    print("2. Consultar Funcionário")
    print("3. Sair")
    
    opcao = input("Escolha uma opção (1, 2 ou 3): ")
    
    if opcao == '1':
        adicionar_funcionario_simples()
    elif opcao == '2':
        consultar_funcionario_simples()
    elif opcao == '3':
        break
    else:
        print("Opção inválida. Tente novamente.")