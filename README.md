# # 📦 Sistema de Controle de Estoque para Pequena Loja (Python)

## 🌟 Sobre o Projeto

Este projeto consiste em um sistema simples de gerenciamento de estoque, desenvolvido em Python, com interface de linha de comando (CLI). O objetivo é informatizar o controle de produtos de uma pequena loja, permitindo o cadastro, a visualização, a busca, a atualização e a exclusão de itens do estoque.

O sistema foi desenvolvido como trabalho prático da disciplina [**Python**] pela dupla:
* [Icaro Ryan/icar0x]
* [Artur alves/Artur-Alves7]

## ✨ Funcionalidades

O sistema apresenta um menu interativo que permite realizar as seguintes operações:

1.  **Cadastrar Produto:** Adiciona um novo item ao estoque.
2.  **Listar Produtos:** Exibe todos os produtos cadastrados com seus detalhes.
3.  **Buscar Produto:** Permite encontrar um produto específico pelo código ou nome.
4.  **Atualizar Produto:** Modifica as informações (nome, preço, quantidade, etc.) de um produto existente.
5.  **Excluir Produto:** Remove um produto do estoque.
6.  **Sair:** Encerra a execução do sistema.

## ⚙️ Estrutura de Dados e Requisitos Atendidos

O projeto foi construído utilizando as seguintes estruturas de dados e conceitos de Python:

| Requisito | Estrutura Utilizada | Propósito |
| :--- | :--- | :--- |
| **Produto** | **Dicionário (`dict`)** | Armazena os dados de um único produto (`codigo`, `nome`, `preco`, `quantidade`). |
| **Estoque** | **Lista (`list`)** | Armazena todos os dicionários de produtos cadastrados. |
| **Controle de Código** | **Conjunto (`set`)** | Garante que os códigos de produtos sejam únicos, evitando duplicatas. |
| **Categorias** | **Tupla (`tuple`)** | Lista imutável de categorias disponíveis (Ex: `("Alimentos", "Limpeza", "Bebidas")`). |
| **Fluxo de Sistema** | **`while` loop** | Mantém o menu principal em execução até que o usuário escolha sair. |
| **Manipulação de Dados** | **`for` loop** | Utilizado para listar produtos e iterar sobre a lista de estoque em buscas e atualizações. |
