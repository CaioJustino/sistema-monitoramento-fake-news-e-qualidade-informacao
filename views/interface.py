"""
views/view_noticia.py

Módulo responsável pela interface de interação para o usuário.
"""

from controllers.controller_noticia import ControllerNoticia
from models.noticia import Noticia

controller = ControllerNoticia()


def listar_noticias():
    """
    Exibe todas as notícias armazenadas no repositório.

    Caso não haja nenhuma notícia cadastrada, exibe uma mensagem de aviso.
    """
    noticias = controller.listar_noticias

    if not noticias:
        print("\nNenhuma notícia cadastrada.")
        return

    print("\n-------------------")
    for noticia in noticias:
        print("Texto:", noticia.texto)
        print("Classificação:", noticia.classificacao)
        print("-------------------")


def add_manual():
    """
    Solicita ao usuário o texto e a classificação da notícia de forma manual.

    Caso a classificação não seja informada, por valor padrão a notícia é classificada como 'Duvidosa'.

    Raises:
        TypeError: Se o texto ou classificação não forem strings.
        ValueError: Se o texto ou classificação estiverem vazios ou a classificação for inválida.
    """
    texto = input("\nDigite o texto: ")
    classificacao = input("Digite a classificação (deixe em branco para 'Duvidosa'): ")

    if classificacao == "":
        classificacao = "Duvidosa"

    try:
        noticia = Noticia(texto, classificacao)
        controller.salvar_noticia(noticia)
        print("\nNotícia salva com sucesso!")
    except (TypeError, ValueError) as e:
        print(f"\nErro ao salvar notícia: {e}")


def add_auto():
    """
    Solicita ao usuário o texto da notícia e define a classificação automaticamente.

    A classificação é determinada por meio de algumas análises,
    com base em critérios como: presença de termos suspeitos e quantidade de caracteres no texto.

    Raises:
        TypeError: Se o texto não for uma string.
        ValueError: Se o texto estiver vazio.
    """
    texto = input("\nDigite o texto: ")

    try:
        classificacao = controller.analisar_texto_noticia(texto)
        noticia = Noticia(texto, classificacao)
        controller.salvar_noticia(noticia)
        print(f"\nNotícia salva com classificação automática: {classificacao}!")
    except (TypeError, ValueError) as e:
        print(f"\nErro ao salvar notícia: {e}")


def menu():
    """
    Exibe o menu disponibilizando a navegação entre as opções disponíveis.

    O menu é exibido em loop em cada escolha até que o usuário escolha a opção de saída.
    """
    while True:
        print("\n1 - Adicionar manualmente")
        print("2 - Adicionar com classificação automática")
        print("3 - Listar notícias")
        print("4 - Sair")

        op = input("Opção: ")

        if op == "1":
            add_manual()
        elif op == "2":
            add_auto()
        elif op == "3":
            listar_noticias()
        elif op == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")