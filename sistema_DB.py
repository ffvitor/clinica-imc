import sqlite3

def criar_tabela_clientes():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    altura REAL NOT NULL,
    peso REAL NOT NULL)
    """)
    conexao.commit()

def adicionar_clientes(clientes):
    cursor.executemany('''
    INSERT INTO clientes (nome, idade, altura, peso)
    VALUES (?, ?, ?, ?)
    ''', clientes)
    conexao.commit()

def adicionar_cliente(nome_cliente, idade_cliente, altura_cliente, peso_cliente):
    """
    Funcao que adiciona cliente na base de dados.
    :param nome_cliente: nome
    :param idade_cliente: idade
    :param altura_cliente: altura
    :param peso_cliente: peso
    :return: None
    """
    cursor.execute('''
    INSERT INTO clientes(nome, idade, altura, peso)
    VALUES(?, ?, ?, ?)
    ''', (nome_cliente, idade_cliente, altura_cliente, peso_cliente))
    conexao.commit()

def consultar_imc(nome_cliente):
    cursor.execute('''
    SELECT nome, altura, peso 
    FROM clientes
    where nome = ?
    ''', (nome_cliente,))
    cliente = cursor.fetchone()

    if cliente:
        nome, altura, peso = cliente
        imc = peso / (altura ** 2)
        return f"0 usuario: {nome} tem IMC = {imc:.2f}"
    else:
        return "cliente nao encontrado"

def usuario_consulta_imc():
    print('\nInforme abaixo o nome para calcular o imc: ')
    nome_pesquisa = input("Digite o nome:")
    print(consultar_imc(nome_pesquisa))

def usuario_adiciona_cliente():
    print('Informe os dados para cadastrar o novo cliente: ')
    nome = input('Digite o nome: ')
    idade = input('Digite a idade: ')
    altura = input('Digite a altura: ')
    peso = input('Digite o peso: ')
    adicionar_cliente(nome, idade, altura, peso)
    print('Cliente cadastrado com sucesso!')

def consultar_cadastro(nome_para_consultar):
    cursor.execute('''
        SELECT nome 
        FROM clientes
        where nome = ?
        ''', (nome_para_consultar,))
    cliente = cursor.fetchone()
    if cliente:
        return 'Cliente encontrado'
    else:
        return 'Cliente nao encontrado'

def usuario_consulta_cadastro():
    print('Informe o nome do cliente a ser pesquisado no sistema: ')
    nome_consulta = input('Digite o nome: ')
    print(consultar_cadastro(nome_consulta))
    return nome_consulta

def app():
    nome_cliente = usuario_consulta_cadastro()
    if 'Cliente encontrado' != consultar_cadastro(nome_cliente):
        usuario_adiciona_cliente()
        print(consultar_imc(nome_cliente))
    else:
        print(consultar_imc(nome_cliente))

if __name__ == '__main__':
    conexao = sqlite3.connect('clinica.db')
    cursor = conexao.cursor()
#sistema
    criar_tabela_clientes()

    clientes = [
        ('Vitor', 25, 1.60, 60),
        ('Carol', 25, 1.67, 60),
        ('Junior', 23, 1.78, 98),
        ('Luan', 89, 1.43, 79),
        ('Laura', 12, 1.33, 34),
    ]
    adicionar_clientes(clientes)
#usuario
    app()
    