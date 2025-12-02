## 🛒 Sistema de Gerenciamento de Produtos

Este sistema em Python permite cadastrar, listar, atualizar e excluir produtos de forma simples e interativa, diretamente pelo terminal.
Foi desenvolvido para facilitar o controle básico de estoque de uma pequena loja.

## ⚙️ Funcionalidades

O sistema apresenta um menu interativo, que permanece ativo até o usuário escolher sair.

Menu principal:
******************************
            MENU
    1 - Cadastrar produto
    2 - Listar produtos
    3 - Atualizar produto
    4 - Excluir produto
    0 - Sair
******************************



## 🧩 Opções do Menu
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

## 🧠 Estrutura Interna

produtos → Lista que armazena os produtos cadastrados.

codigo_cad → Conjunto usado para garantir códigos únicos.

categorias → Tupla com as categorias disponíveis.

## 🧱 Funções principais:

cadastrar_produto()

listar_produtos()

atualizar_produto()

excluir_produto()





## 🎓 Sistema de Controle de Alunos e Notas

Este sistema em Python permite cadastrar alunos, registrar notas, calcular médias e exibir relatórios de desempenho.
Foi desenvolvido para auxiliar professores no acompanhamento das notas e aprovação dos alunos de forma prática e interativa, diretamente pelo terminal.

## ⚙️ Funcionalidades

O sistema apresenta um menu interativo, que permanece ativo até o usuário escolher sair.

##      Menu
1 - Cadastrar aluno

2 - Registrar notas

3 - Listar alunos e médias

4 - Buscar aluno

5 - Mostrar aprovados e reprovados

6 - Relatórios

0 - Sair


## 🧩 Opções do Menu
📝 1 - Cadastrar aluno

Permite registrar um novo aluno no sistema.
Durante o cadastro, o usuário informa:

Matrícula (identificador único do aluno)

Nome completo do aluno

⚠️ Caso o aluno já esteja cadastrado, o sistema exibirá uma mensagem de erro e não fará o registro.

Exemplo de uso:

Digite a matrícula do aluno: A001

Digite o nome do aluno: Ana Silva

✅ Aluno 'Ana Silva' cadastrado com sucesso!

✍️ 2 - Registrar notas

Permite registrar até 3 notas para um aluno já cadastrado.
As notas devem ser valores entre 0 e 10.

⚠️ Caso a matrícula não exista, o sistema exibirá uma mensagem de erro.

Exemplo de uso:

Digite a matrícula do aluno: A001

Digite a 1ª nota: 8.0

Digite a 2ª nota: 7.5

Digite a 3ª nota: 9.0

✅ Notas registradas com sucesso!

📋 3 - Listar alunos e médias

Mostra todos os alunos cadastrados, suas notas e a média final calculada automaticamente.

Exemplo de saída:

=== LISTA DE ALUNOS E MÉDIAS ===

Matrícula: A001 | Notas: (8.0, 7.5, 9.0) | Média: 8.17

Matrícula: A002 | Notas: (5.0, 6.0, 5.5) | Média: 5.50

Se nenhum aluno estiver cadastrado:

Nenhum aluno cadastrado.

🔍 4 - Buscar aluno

Permite consultar um aluno específico a partir de sua matrícula.
O sistema exibe as notas e a média do aluno.

Exemplo de uso:

Digite a matrícula do aluno: A001
📘 Aluno encontrado! Notas: (8.0, 7.5, 9.0) | Média: 8.17


Caso a matrícula não exista:

❌ Aluno não encontrado.

🏆 5 - Mostrar aprovados e reprovados

Exibe todos os alunos com suas médias e situação final:

Aprovado ✅: média ≥ 7

Reprovado ❌: média < 7

Exemplo de saída:

=== RESULTADO FINAL ===

Matrícula: A001 | Média: 8.17 | Aprovado ✅

Matrícula: A002 | Média: 5.50 | Reprovado ❌

📊 6 - Relatórios

Gera relatórios automáticos conforme a opção escolhida:

Alunos cadastrados

Médias individuais

Aprovados e Reprovados

Exemplo:

=== RELATÓRIOS ===

1 - Alunos cadastrados

2 - Médias individuais

3 - Aprovados e Reprovados

Escolha uma opção: 2

=== LISTA DE ALUNOS E MÉDIAS ===

Matrícula: A001 | Notas: (8.0, 7.5, 9.0) | Média: 8.17

🚪 0 - Sair

Finaliza o programa exibindo uma mensagem de despedida:

Saindo do sistema...

## 🧠 Estrutura Interna
| Estrutura                   | Função                                                                                   |
| --------------------------- | ---------------------------------------------------------------------------------------- |
| **alunos (dict)**           | Dicionário principal que armazena as matrículas e notas. Ex: `{"A001": (8.0, 7.5, 9.0)}` |
| **nomes_cadastrados (set)** | Conjunto usado para evitar duplicatas de alunos.                                         |
| **listas temporárias**      | Usadas para coletar notas antes de transformá-las em tuplas.                             |

## 🧱 Funções principais

cadastrar_aluno() → Registra um novo aluno.

registrar_notas() → Adiciona as notas do aluno.

listar_alunos_medias() → Exibe alunos com suas médias.

buscar_aluno() → Busca um aluno por matrícula.

mostrar_aprovados_reprovados() → Exibe a situação final.

relatorios() → Gera relatórios de desempenho.
