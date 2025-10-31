from time import sleep
from decimal import Decimal


produtos = []  
codigo_cad = set()  
categorias = ("Comida", "Limpeza", "Bebidas", "Higiene", "Cosméticos")  


def cadastrar_produto():
    try:
        
        codigo = int(input("Digite o código do produto: "))

      
        if codigo in codigo_cad:
            print(" Código já cadastrado! Tente outro.")
            return  # Sai da função sem cadastrar o produto

       
        nome = input("Digite o nome do produto: ").strip()
        preco = Decimal(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade em estoque: "))

        # Mostra todas as categorias disponíveis numeradas
        print("Categorias disponíveis:")
        for i, cat in enumerate(categorias, start=1):  # enumera() gera número e item
            print(f"{i} - {cat}")

        
        escolha = int(input("Escolha a categoria (número): "))

        # Verifica se o número digitado está dentro do intervalo válido
        if escolha < 1 or escolha > len(categorias):
            print(" Categoria inválida!")
            return

        # Pega o nome da categoria com base no número escolhido
        categoria = categorias[escolha - 1]

        
        produto = {
            "codigo": codigo,
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade,
            "categoria": categoria
        }

        
        produtos.append(produto)
        codigo_cad.add(codigo)

        print(" Produto cadastrado com sucesso!")
        sleep(1)  

    
    except ValueError:
        print(" Valor inválido! Digite corretamente.")


def listar_produtos():
    # Verifica se a lista está vazia
    if not produtos:
        print(" Nenhum produto cadastrado.")
        return

    # Exibe todos os produtos de forma formatada
    print(" Lista de produtos:")
    for p in produtos:
        print(f"Código: {p['codigo']} | Nome: {p['nome']} | Preço: R${p['preco']:.2f} | "
              f"Qtd: {p['quantidade']} | Categoria: {p['categoria']}")
    print()  


def atualizar_produto():
    try:
        
        codigo = int(input("Digite o código do produto que deseja atualizar: "))

        # Procura o produto na lista
        for p in produtos:
            if p["codigo"] == codigo:
                print(f"Produto atual: {p}")

                # Atualiza o nome (ou mantém se o usuário apertar Enter)
                p["nome"] = input("Novo nome (ou Enter para manter): ") or p["nome"]

                # Atualiza o preço (somente se o usuário digitar algo)
                novo_preco = input("Novo preço (ou Enter para manter): ")
                if novo_preco:
                    p["preco"] = float(novo_preco)

                # Atualiza a quantidade (somente se o usuário digitar algo)
                nova_qtd = input("Nova quantidade (ou Enter para manter): ")
                if nova_qtd:
                    p["quantidade"] = int(nova_qtd)

                print("Produto atualizado com sucesso!")
                return  # Sai da função após atualizar

        # Se o código não for encontrado
        print(" Produto não encontrado.")

    except ValueError:
        print(" Entrada inválida!")


def excluir_produto():
    try:
        # Solicita o código do produto a ser removido
        codigo = int(input("Digite o código do produto que deseja excluir: "))

        # Procura o produto na lista
        for p in produtos:
            if p["codigo"] == codigo:
                produtos.remove(p)  # Remove da lista
                codigo_cad.remove(codigo)  # Remove do conjunto de códigos
                print(" Produto excluído com sucesso!\n")
                return

        
        print(" Produto não encontrado")

    except ValueError:
        print(" Entrada inválida!")


while True:
    titulo = "Menu"
    print("*" * 30)
    print(titulo.upper().center(30))
    print("*" * 30)
    print("""
    1 - Cadastrar produto
    2 - Listar produtos
    3 - Atualizar produto
    4 - Excluir produto
    0 - Sair
    """)

    opcao = input("Qual opção você deseja? ").lower().strip()

    # Verifica o que o usuário digitou e chama a função correspondente
    if opcao in ("1", "cadastrar", "cadastrar produto"):
        cadastrar_produto()
    elif opcao in ("2", "listar", "listar produtos"):
        listar_produtos()
    elif opcao in ("3", "atualizar", "atualizar produto"):
        atualizar_produto()
    elif opcao in ("4", "excluir", "excluir produto"):
        excluir_produto()
    elif opcao in ("0", "sair"):
        print("Saindo do sistema...")
        sleep(1)
        print("Obrigado pelo uso do sistema, volte sempre!")
        break  # Encerra o loop principal (fecha o sistema)
    print(" Opção inválida, tente novamente!")
