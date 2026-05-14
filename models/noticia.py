"""
models/noticia.py

Módulo responsável pela definição das classes domínio para notícias.
"""

class ClassificacaoNoticia:
    """
    Classe que define as classificações possíveis para uma notícia.

    Atributos:
        opcoes_classificacao (list): Lista com as classificações válidas:
            'Duvidosa', 'Confiavel' e 'Falsa'.
    """

    opcoes_classificacao = ["Duvidosa", "Confiável", "Falsa"]

    @staticmethod
    def resgatar_opcoes_classificacao():
        return ClassificacaoNoticia.opcoes_classificacao

class Noticia:
    """
    Classe que representa uma notícia com texto e classficação.

    Atributos:
        Texto (str): 0 conteúdo textual da notícia.
        classificacao (str): A classificação da notícia ('Duvidosa', 'Confiável' ou 'Falsa').

    Raises:
        TypeError: Se o texto ou classificação não forem strings.
        ValueError: Se o texto ou classificação estiverem vazios, ou se a classificação não for uma das opções válidas.
    """

    def __init__(self, texto, classificacao):
        """
        Args:
            texto (str): O conteúdo textual da notícia.
            classificação (str): A classificação da notícia.

        Raises:
            TypeError: Se texto ou classificação não forem strings.
            ValueError: Se o texto ou classificação estiverem vazios, ou se a classificação não pertencer as opções válidas.
        """
        
        if not isinstance(texto, str):
            raise TypeError("O texto da notícia precisa ser do tipo 'string'.")
        
        elif not isinstance(classificacao, str):
            raise TypeError("A classificação da notícia precisa ser do tipo 'string'.")
        
        elif not texto or not texto.strip():
            raise ValueError("O texto da notícia está vazio.")

        elif classificacao not in ClassificacaoNoticia.resgatar_opcoes_classificacao():
            raise ValueError("A notícia só pode ser classificada como Duvidosa, Confiável ou Falsa.")

        self.__texto = texto
        self.__classificacao = classificacao

    @property
    def texto(self):
        return self.__texto
    
    @property
    def classificacao(self):
        return self.__classificacao
    
    @texto.setter
    def texto(self, texto):
        self.__texto = texto
    
    @classificacao.setter
    def classificacao(self, classificacao):
        self.__classificacao = classificacao
