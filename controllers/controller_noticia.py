from models.noticia import Noticia, ClassificacaoNoticia

class ControllerNoticia:
    TERMOS_SUSPEITOS = ["URGENTE", "!!!"]
    LIMITE_MINIMO_TEXTO = 10

    def __init__(self):
        self.__repositorio_noticias = []

    @property
    def listar_noticias(self):
        return self.__repositorio_noticias

    def analisar_texto_noticia(self, texto):
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
        opcoes_classificacao = ClassificacaoNoticia.resgatar_opcoes_classificacao()

        if not isinstance(noticia, Noticia):
            raise TypeError("O objeto precisa ser uma instância da classe Notícia.")

        elif noticia.classificacao not in opcoes_classificacao:
            noticia.classificacao = "Duvidosa"

        self.__repositorio_noticias.append(noticia)
        return True