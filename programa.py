import json


def carregar_dados():
    try:
        with open("pessoas.json", "r") as arquivo:
            return json.load(arquivo)
    except:
        return []


def salvar_dados(pessoas):
    with open("pessoas.json", "w") as arquivo:
        json.dump(pessoas, arquivo)


def nome_ja_existe(pessoas, nome):
    for pessoa in pessoas:
        if pessoa["nome"].lower() == nome.lower():
            return True
    return False


def cadastrar_pessoa(pessoas):
    while True:
        nome = input("Digite o nome: ").strip()

        if nome == "":
            print("O nome não pode ficar vazio.")
        elif nome_ja_existe(pessoas, nome):
            print("Já existe uma pessoa cadastrada com esse nome.")
        else:
            break

    while True:
        idade_texto = input("Digite a idade: ").strip()

        if idade_texto.isdigit():
            idade = int(idade_texto)
            break
        else:
            print("Digite apenas números para a idade.")

    pessoa = {
        "nome": nome,
        "idade": idade
    }

    pessoas.append(pessoa)
    print("Pessoa cadastrada com sucesso!")


def listar_pessoas(pessoas):
    if len(pessoas) == 0:
        print("Nenhuma pessoa cadastrada.")
    else:
        print("\n=== PESSOAS CADASTRADAS ===")
        for pessoa in pessoas:
            print("Nome:", pessoa["nome"], "| Idade:", pessoa["idade"])


def buscar_pessoa(pessoas):
    nome_busca = input("Digite o nome que deseja buscar: ").strip()
    encontrado = False

    for pessoa in pessoas:
        if pessoa["nome"].lower() == nome_busca.lower():
            print("Nome:", pessoa["nome"], "| Idade:", pessoa["idade"])
            encontrado = True

    if not encontrado:
        print("Pessoa não encontrada.")


def remover_pessoa(pessoas):
    nome_remover = input("Digite o nome que deseja remover: ").strip()
    encontrado = False

    for i in range(len(pessoas)):
        if pessoas[i]["nome"].lower() == nome_remover.lower():
            pessoas.pop(i)
            print("Pessoa removida com sucesso!")
            encontrado = True
            break

    if not encontrado:
        print("Pessoa não encontrada.")


def editar_pessoa(pessoas):
    nome_busca = input("Digite o nome da pessoa que deseja editar: ").strip()

    for pessoa in pessoas:
        if pessoa["nome"].lower() == nome_busca.lower():
            print("Pessoa encontrada:")
            print("Nome atual:", pessoa["nome"])
            print("Idade atual:", pessoa["idade"])

            novo_nome = input("Digite o novo nome: ").strip()

            while True:
                nova_idade_texto = input("Digite a nova idade: ").strip()

                if nova_idade_texto.isdigit():
                    nova_idade = int(nova_idade_texto)
                    break
                else:
                    print("Digite apenas números para a idade.")

            pessoa["nome"] = novo_nome
            pessoa["idade"] = nova_idade

            print("Pessoa editada com sucesso!")
            return

    print("Pessoa não encontrada.")


def mostrar_menu():
    print("\n" + "=" * 35)
    print("   SISTEMA DE CADASTRO DE PESSOAS")
    print("=" * 35)
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Buscar pessoa")
    print("4 - Remover pessoa")
    print("5 - Editar pessoa")
    print("6 - Sair")


def main():
    pessoas = carregar_dados()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_pessoa(pessoas)

        elif opcao == "2":
            listar_pessoas(pessoas)

        elif opcao == "3":
            buscar_pessoa(pessoas)

        elif opcao == "4":
            remover_pessoa(pessoas)

        elif opcao == "5":
            editar_pessoa(pessoas)

        elif opcao == "6":
            salvar_dados(pessoas)
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


main()