🛒 Sistema de Gerenciamento de Produtos

Este sistema em Python permite cadastrar, listar, atualizar e excluir produtos de forma simples e interativa, diretamente pelo terminal.
Foi desenvolvido para facilitar o controle básico de estoque de uma pequena loja.

⚙️ Funcionalidades

O sistema apresenta um menu interativo, que permanece ativo até o usuário escolher sair.

Menu principal:
******************************
            MENU
******************************

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

Categoria (selecionada de uma lista pré-definida)

⚠️ Caso o código já esteja cadastrado, o sistema exibirá uma mensagem de erro e não fará o registro.

Exemplo de uso:

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

Mostra todos os produtos cadastrados com informações completas:

Código: 101 | Nome: Arroz Integral | Preço: R$12.50 | Qtd: 20 | Categoria: Comida


Se nenhum produto estiver cadastrado, o sistema informará:

Nenhum produto cadastrado.

✏️ 3 - Atualizar produto

Permite modificar as informações de um produto existente.
O usuário pode alterar:

Nome

Preço

Quantidade

Caso não queira alterar um campo, basta pressionar Enter para manter o valor atual.

Exemplo de uso:

Digite o código do produto que deseja atualizar: 101
Produto atual: {'codigo': 101, 'nome': 'Arroz Integral', 'preco': 12.5, 'quantidade': 20, 'categoria': 'Comida'}
Novo nome (ou Enter para manter): Arroz Integral 1kg
Novo preço (ou Enter para manter): 13.00
Nova quantidade (ou Enter para manter): 25
Produto atualizado com sucesso!

🗑️ 4 - Excluir produto

Remove um produto do sistema com base no seu código.

Exemplo de uso:

Digite o código do produto que deseja excluir: 101
Produto excluído com sucesso!


Caso o código não exista:

Produto não encontrado

🚪 0 - Sair

Finaliza o programa exibindo uma mensagem de despedida:

Saindo do sistema...
Obrigado pelo uso do sistema, volte sempre!

🧠 Estrutura Interna

produtos → Lista que armazena os produtos cadastrados.

codigo_cad → Conjunto usado para garantir códigos únicos.

categorias → Tupla com as categorias disponíveis.

Funções principais:

cadastrar_produto()

listar_produtos()

atualizar_produto()

excluir_produto()





## 🎓 Sistema de Controle de Alunos e Notas (Python)

## 🌟 Sobre o Projeto

Este projeto consiste em um sistema simples de controle de alunos e notas, desenvolvido em Python, com interface de linha de comando (CLI). O objetivo é ajudar professores a registrar alunos, lançar notas e calcular médias automaticamente, facilitando o acompanhamento do desempenho da turma.

## ✨ Funcionalidades

O sistema apresenta um menu interativo, permitindo realizar as seguintes operações:

1. **Cadastrar Aluno** – Registra um novo aluno no sistema.
2. **Registrar Notas** – Adiciona as notas de um aluno cadastrado.
3. **Listar Alunos e Médias** – Exibe todos os alunos cadastrados com suas respectivas médias.
4. **Buscar Aluno** – Permite localizar um aluno específico pelo nome ou matrícula.
5. **Mostrar Aprovados e Reprovados** – Exibe alunos classificados conforme o desempenho (média ≥ 7: aprovado).
6. **Relatórios** – Gera relatórios com diferentes informações: lista de alunos cadastrados, médias individuais e alunos aprovados e reprovados.
7. **Sair** – Encerra a execução do sistema.

## ⚙️ Estrutura de Dados e Requisitos Atendidos

| Requisito              | Estrutura Utilizada     | Propósito                                                                               |
| :--------------------- | :---------------------- | :-------------------------------------------------------------------------------------- |
| **Aluno**              | **Dicionário (`dict`)** | Armazena a matrícula como chave e as notas como valor. Ex: `{ "Ana": (8.0, 7.5, 9.0) }` |
| **Notas Temporárias**  | **Lista (`list`)**      | Guarda as notas antes de convertê-las em tupla.                                         |
| **Controle de Alunos** | **Conjunto (`set`)**    | Evita cadastros duplicados de alunos.                                                   |
| **Notas Finais**       | **Tupla (`tuple`)**     | Armazena as notas de forma imutável.                                                    |
| **Cálculo de Médias**  | **`for` loop**          | Percorre as notas dos alunos para calcular e exibir médias.                             |
| **Menu Interativo**    | **`while` loop**        | Mantém o sistema em execução até o usuário escolher sair.                               |

