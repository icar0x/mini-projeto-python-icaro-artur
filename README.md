## 🐍 Mini Projetos em Python – Sistemas de Controle

## 📘 Sobre o Repositório

Este repositório contém dois sistemas desenvolvidos em Python, com interface de linha de comando (CLI), como parte da disciplina Programação I – Python, no curso de Engenharia de Software.

Os projetos foram criados com o objetivo de aplicar estruturas de repetição, estruturas de dados e lógica de programação para resolver problemas práticos do dia a dia.

Desenvolvido pela dupla:
* Icaro Ryan / icar0x
* Artur Alves / Artur-Alves7


# # 📦 Sistema de Controle de Estoque para Pequena Loja (Python)

## 🌟 Sobre o Projeto

Este projeto consiste em um sistema simples de gerenciamento de estoque, desenvolvido em Python, com interface de linha de comando (CLI). O objetivo é informatizar o controle de produtos de uma pequena loja, permitindo o cadastro, a visualização, a busca, a atualização e a exclusão de itens do estoque.

## ✨ Funcionalidades

O sistema apresenta um menu interativo que permite realizar as seguintes operações:

1.  **Cadastrar Produto:** Adiciona um novo item ao estoque.
2.  **Listar Produtos:** Exibe todos os produtos cadastrados com seus detalhes.
3.  **Buscar Produto:** Permite encontrar um produto específico pelo código ou nome.
4.  **Atualizar Produto:** Modifica as informações (nome, preço, quantidade, etc.) de um produto existente.
5.  **Excluir Produto:** Remove um produto do estoque.
6.  **Sair:** Encerra a execução do sistema.

## ⚙️ Estrutura de Dados e Requisitos Atendidos

| Requisito                | Estrutura Utilizada     | Propósito                                                                                  |
| :----------------------- | :---------------------- | :----------------------------------------------------------------------------------------- |
| **Produto**              | **Dicionário (`dict`)** | Armazena os dados de um único produto (`codigo`, `nome`, `preco`, `quantidade`).           |
| **Estoque**              | **Lista (`list`)**      | Armazena todos os dicionários de produtos cadastrados.                                     |
| **Controle de Código**   | **Conjunto (`set`)**    | Garante que os códigos de produtos sejam únicos, evitando duplicatas.                      |
| **Categorias**           | **Tupla (`tuple`)**     | Lista imutável de categorias disponíveis (Ex: `("Alimentos", "Limpeza", "Bebidas")`).      |
| **Fluxo de Sistema**     | **`while` loop**        | Mantém o menu principal em execução até que o usuário escolha sair.                        |
| **Manipulação de Dados** | **`for` loop**          | Utilizado para listar produtos e iterar sobre a lista de estoque em buscas e atualizações. |





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

