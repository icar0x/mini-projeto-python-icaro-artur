⚙️ Funcionalidades do Sistema

O sistema funciona através de um menu interativo que permanece ativo até o usuário escolher sair.

📌 Menu Principal
1 - Cadastrar produto
2 - Listar produtos
3 - Atualizar produto
4 - Excluir produto
0 - Sair

🧩 Opções do Menu
📝 1 - Cadastrar produto

Permite registrar um novo produto no sistema.
Durante o cadastro, o usuário informa:

Código do produto (número único)

Nome do produto

Preço

Quantidade em estoque

Categoria (escolhida de uma lista exibida na tela)

✔️ Exemplo
Digite o código do produto: 101
Digite o nome do produto: Arroz Integral
Digite o preço do produto: 12.50
Digite a quantidade em estoque: 20

Categorias disponíveis:
1 - Comida
2 - Limpeza
3 - Bebidas
4 - Higiene
5 - Cosméticos

Escolha a categoria (número): 1

Produto cadastrado com sucesso!

📋 2 - Listar produtos

Exibe todos os produtos cadastrados com informações completas:

Código: 101 | Nome: Arroz Integral | Preço: R$ 12.50 | Qtd: 20 | Categoria: Comida


Caso não exista nenhum produto, o sistema informa:

Nenhum produto cadastrado.

✏️ 3 - Atualizar produto

Permite modificar:

Nome

Preço

Quantidade

⚠️ Campos opcionais:
Se o usuário pressionar Enter sem digitar nada, o valor atual será mantido.

✔️ Exemplo
Digite o código do produto que deseja atualizar: 101

Produto atual:
{'codigo': 101, 'nome': 'Arroz Integral', 'preco': 12.5, 'quantidade': 20, 'categoria': 'Comida'}

Novo nome (ou Enter para manter): Arroz Integral 1kg
Novo preço (ou Enter para manter): 13.00
Nova quantidade (ou Enter para manter): 25

Produto atualizado com sucesso!


Caso o código não exista:

Produto não encontrado.

🗑️ 4 - Excluir produto

Remove um produto do sistema com base no seu código.

✔️ Exemplo
Digite o código do produto que deseja excluir: 101
Produto excluído com sucesso!


Se o código não existir:

Produto não encontrado.

🚪 0 - Sair

Finaliza o programa exibindo:

Saindo do sistema...
Obrigado pelo uso do sistema, volte sempre!

🧠 Estrutura Interna
Armazenamento

O sistema utiliza JSON para salvar os dados:

produtos.json

Estruturas usadas:
Estrutura	Função
produtos (list)	Armazena todos os produtos cadastrados
codigos (set)	Garante que não existem códigos duplicados
categorias (tuple)	Lista de categorias disponíveis para seleção
🧱 Funções Principais
✔ cadastrar_produto()

Registra um novo produto com validação de campos e código único.

✔ listar_produtos()

Exibe todos os produtos em formato legível.

✔ atualizar_produto()

Atualiza dados sem obrigar usuário a reescrever tudo.

✔ excluir_produto()

Remove um produto conforme seu código.

📂 Estrutura de Pastas do Projeto
seu_projeto/
│── produtos.json
│── __init__.py
│── funcoes.py
│── main.py
│── README.md
