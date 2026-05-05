"""
controllers/controller_noticia.py

Módulo responsável pelo controle e gerenciamento de notícias

Classes:
    ControllerNoticia: Controlador principal para análise, salvamento e listagem de notícias.
"""

from models.noticia import Noticia, ClassificacaoNoticia

class ControllerNoticia:
    """
    Controlador responsável por gerenciar as operações relacionadas a notícias.

    Atributos de Classe:
        TERMOS_SUSPEITOS (list): Termos que indicam possível notícia falsa ou duvidosa.
        LIMITE_MINIMO_TEXTO (int): Quantidade mínima de caracteres que um texto deve ter.    
    """

    TERMOS_SUSPEITOS = ["URGENTE", "!!!"]
    LIMITE_MINIMO_TEXTO = 10

    def __init__(self):
        """Inicializa o controlador com um repositório de notícias vazio."""
        self.__repositorio_noticias = []

    @property
    def listar_noticias(self):
        """list: Rteorna a lista de notícias salvas no repositório."""
        return self.__repositorio_noticias

    def analisar_texto_noticia(self, texto):
        """
        Analisa o texto de uma notícia e retorna uma classificação automática.

        A classificação é baseada em um sistema de pontuação que verifica
        a presença de termos suspeitos e o tamanho mínimo do texto.

        Args:
            texto (str): O texto da notícia a ser analisado.

        Returns:
            str: A classificação da notícia, podendo ser:
                - 'Confiável': nenhum critério suspeito encontrado.
                - 'Duvidosa': um critério suspeito encontrado.
                - 'Falsa': dois critérios suspeitos encontrados.

        Raises:
            TypeError: Se o texto não for uma string.
            ValueError: Se o texto estiver vazio ou contiver apenas espaços.
        """

        if not isinstance(texto, str):
            raise TypeError("O texto da notícia precisa ser do tipo 'string'.")
        
        elif not texto or not texto.strip():
            raise ValueError("O texto da notícia está vazio.")

        pontuacao_noticia_falsa = 0

        if any(termo in texto for termo in self.TERMOS_SUSPEITOS):
            pontuacao_noticia_falsa += 1

        if len(texto) < self.LIMITE_MINIMO_TEXTO:
            pontuacao_noticia_falsa += 1

        if pontuacao_noticia_falsa == 0:
            return "Confiável"
        
        elif pontuacao_noticia_falsa == 1:
            return "Duvidosa"
        
        return "Falsa"

    def salvar_noticia(self, noticia):
        """
        Valida e salva uma notícia no repositório.

        Se a classificação da notícia não for válida, ela é corrigida
        automaticamente para 'Duvidosa' antes de ser salva.

        Args:
            noticia (Noticia): O objeto notícia a ser salvo.

        Returns:
            bool: True se a notícia for salva com sucesso.

        Raises:
            TypeError: Se o objeto fornecido não for uma instância de Noticia.
        """

        opcoes_classificacao = ClassificacaoNoticia.resgatar_opcoes_classificacao()

        if not isinstance(noticia, Noticia):
            raise TypeError("O objeto precisa ser uma instância da classe Notícia.")

        elif noticia.classificacao not in opcoes_classificacao:
            noticia.classificacao = "Duvidosa"

        self.__repositorio_noticias.append(noticia)
        return True
    