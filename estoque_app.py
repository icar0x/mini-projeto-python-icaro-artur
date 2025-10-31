from time import sleep  


produtos = [] # para armazenar os produtos cadastrados
codigo_cad = set() # para nao duplicar os codigos
categorias = ("Alimentos", "Limpeza", "Bebidas", "Higiene")

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
 opcao = input("Qual opção voce deseja? ").lower().strip()

 if opcao == "1" or opcao == "cadastrar" or opcao == "cadastrar produto":
  print("Função cadastrar produto selecionado")
  
 elif opcao == "0" or opcao == "sair":
  print("Saindo do sistema...")
  sleep(1)
  print("Obrigado pelo uso do sistema, volte sempre!")
  break
 
 else:
  print("Opção invalida, tente novamente!")