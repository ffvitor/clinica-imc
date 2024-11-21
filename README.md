# Sistema de Gerenciamento de Clientes - Clínica

Este projeto é um sistema simples em Python que gerencia clientes em um banco de dados SQLite. Ele permite adicionar, consultar e calcular o Índice de Massa Corporal (IMC) dos clientes.

## Funcionalidades

- **Criação de tabela**: Cria automaticamente a tabela `clientes` caso ela não exista.
- **Cadastro de clientes**: Adiciona novos clientes à base de dados.
- **Consulta de clientes**: Verifica se um cliente está cadastrado no sistema.
- **Cálculo de IMC**: Calcula o IMC de um cliente com base na altura e peso armazenados.
- **Interatividade**: Permite ao usuário interagir diretamente com o sistema para adicionar e consultar clientes.

## Estrutura da Tabela `clientes`

A tabela é composta pelos seguintes campos:
- **id**: Identificador único do cliente (chave primária).
- **nome**: Nome do cliente (texto).
- **idade**: Idade do cliente (inteiro).
- **altura**: Altura do cliente em metros (número real).
- **peso**: Peso do cliente em quilogramas (número real).

## Como Utilizar

### Requisitos
- Python 3.x
- Biblioteca `sqlite3` (incluída no Python padrão)

### Passos

1. Clone este repositório ou copie o código para um arquivo Python.
2. Execute o script. Ele criará o banco de dados SQLite chamado `clinica.db` e populá-lo-á com alguns dados iniciais.
3. Escolha uma das opções interativas disponíveis:
   - Pesquisar por um cliente e calcular seu IMC.
   - Adicionar um novo cliente caso ele não esteja cadastrado.

### Fluxo Principal
- O sistema verifica se um cliente já está cadastrado.
- Caso o cliente não exista, solicita os dados para cadastro e calcula o IMC.
- Caso o cliente já esteja cadastrado, exibe seu IMC diretamente.

## Estrutura do Código

### Principais Funções

- `criar_tabela_clientes`: Cria a tabela `clientes` no banco de dados.
- `adicionar_clientes`: Insere múltiplos clientes de uma vez.
- `adicionar_cliente`: Insere um único cliente.
- `consultar_imc`: Calcula o IMC de um cliente específico.
- `usuario_consulta_imc`: Solicita o nome de um cliente e retorna o cálculo do IMC.
- `usuario_adiciona_cliente`: Solicita dados do cliente para cadastro.
- `consultar_cadastro`: Verifica se um cliente está cadastrado.
- `usuario_consulta_cadastro`: Interage com o usuário para pesquisar um cliente.
- `app`: Controla o fluxo principal do programa.

## Exemplo de Dados

O sistema é inicializado com os seguintes dados de clientes:

| Nome    | Idade | Altura | Peso |
|---------|-------|--------|------|
| Vitor   | 25    | 1.60   | 60   |
| Carol   | 25    | 1.67   | 60   |
| Junior  | 23    | 1.78   | 98   |
| Luan    | 89    | 1.43   | 79   |
| Laura   | 12    | 1.33   | 34   |
