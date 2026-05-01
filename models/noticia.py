class ClassificacaoNoticia:
    opcoes_classificacao = ["Duvidosa", "Confiável", "Falsa"]

    @staticmethod
    def resgatar_opcoes_classificacao():
        return ClassificacaoNoticia.opcoes_classificacao

class Noticia:
    def __init__(self, texto, classificacao):
        if not isinstance(texto, str):
            raise TypeError("O texto da notícia precisa ser do tipo 'string'.")
        
        elif not isinstance(classificacao, str):
            raise TypeError("A classificação da notícia precisa ser do tipo 'string'.")
        
        elif not texto or not texto.strip():
            raise ValueError("O texto da notícia está vazio.")

        elif not classificacao or not classificacao.strip():
            raise ValueError("A classificação da notícia está vazia.")

        elif classificacao not in ClassificacaoNoticia.get_opcoes_classificacao():
            raise ValueError("A notícia só pode ser classificada como Duvidosa, Confiável ou False.")

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