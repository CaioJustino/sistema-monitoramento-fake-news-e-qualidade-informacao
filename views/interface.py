from controllers.controller_noticia import repositorio_noticias, salvar_noticia, analisar

def func2():
    # lista tudo
    for i in range(0, len(repositorio_noticias)):
        print("Texto:", repositorio_noticias[i]["t"])
        print("Classificacao:", repositorio_noticias[i]["c"])
        print("-------------------")

def add_manual():
    t = input("Digite o texto: ")
    c = input("Digite classificacao: ")

    if c == "":
        salvar_noticia(t)
    else:
        salvar_noticia(t, c)


def add_auto():
    t = input("Digite o texto: ")
    c = analisar(t)
    salvar_noticia(t, c)


def menu():
    while True:
        print("1 - adicionar manual")
        print("2 - adicionar automatico")
        print("3 - listar")
        print("4 - sair")

        op = input("opcao: ")

        if op == "1":
            add_manual()
        elif op == "2":
            add_auto()
        elif op == "3":
            func2()
        elif op == "4":
            break
        else:
            print("errado")


# comentarios desnecessarios abaixo
# inicia o programa
# chama o menu
menu()