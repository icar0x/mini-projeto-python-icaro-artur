def menu():
    print("\n===== SISTEMA DE CONTROLE DE ALUNOS =====")
    print("1 - Cadastrar aluno")
    print("2 - Registrar notas")
    print("3 - Listar alunos e médias")
    print("4 - Buscar aluno")
    print("5 - Mostrar aprovados e reprovados")
    print("6 - Relatórios")
    print("0 - Sair")


alunos = {}
nomes_cadastrados = set()


def cadastrar_aluno():
    matricula = input("Digite a matrícula do aluno: ").strip()
    nome = input("Digite o nome do aluno: ").strip().title()

    if nome in nomes_cadastrados:
        print("Aluno já cadastrado!")
    else:
        alunos[matricula] = ()
        nomes_cadastrados.add(nome)
        print(f"Aluno '{nome}' cadastrado com sucesso!")


def registrar_notas():
    matricula = input("Digite a matrícula do aluno: ").strip()
    if matricula not in alunos:
        print("Matrícula não encontrada!")
        return

    notas_temp = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Digite a {i}ª nota: "))
                if 0 <= nota <= 10:
                    notas_temp.append(nota)
                    break
                else:
                    print("A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Entrada inválida! Digite um número.")

    alunos[matricula] = tuple(notas_temp)
    print("Notas registradas com sucesso!")


def listar_alunos_medias():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("\n=== LISTA DE ALUNOS E MÉDIAS ===")
    for matricula, notas in alunos.items():
        media = sum(notas) / len(notas) if notas else 0
        print(f"Matrícula: {matricula} | Notas: {notas} | Média: {media:.2f}")


def buscar_aluno():
    matricula = input("Digite a matrícula do aluno: ").strip()
    if matricula in alunos:
        notas = alunos[matricula]
        media = sum(notas) / len(notas) if notas else 0
        print(f"Aluno encontrado! Notas: {notas} | Média: {media:.2f}")
    else:
        print("Aluno não encontrado.")


def mostrar_aprovados_reprovados():
    print("\n=== RESULTADO FINAL ===")
    for matricula, notas in alunos.items():
        media = sum(notas) / len(notas) if notas else 0
        status = "Aprovado" if media >= 7 else "Reprovado"
        print(f"Matrícula: {matricula} | Média: {media:.2f} | {status}")


def relatorios():
    print("\n=== RELATÓRIOS ===")
    print("1 - Alunos cadastrados")
    print("2 - Médias individuais")
    print("3 - Aprovados e Reprovados")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\nAlunos cadastrados:")
        for matricula in alunos:
            print(f"- Matrícula: {matricula}")
    elif opcao == "2":
        listar_alunos_medias()
    elif opcao == "3":
        mostrar_aprovados_reprovados()
    else:
        print("Opção inválida!")


while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        registrar_notas()
    elif opcao == "3":
        listar_alunos_medias()
    elif opcao == "4":
        buscar_aluno()
    elif opcao == "5":
        mostrar_aprovados_reprovados()
    elif opcao == "6":
        relatorios()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")
