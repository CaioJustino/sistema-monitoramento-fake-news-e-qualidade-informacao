# Sistema de Monitoramento de Fake News e Qualidade da Informação 

O presente trabalho buscou aplicar conceitos de boas práticas de programação a fim de melhorar um sistema mal estruturado de monitoramento de fake news e qualidade da informação, sem reescrevê-lo do zero.

<br>

## 💻 Funcionalidades do Sistema 
<br>

📰 **Inserir textos de notícias**
- Realiza o cadastro de notícias.

🔎 **Classificação das Notícias**
- O sistema classifica as notícias como confiável, duvidosa ou falsa.
  
📝 **Listar as notícias**
- Faz a listagens das notícias cadastradas.

<br><br>

## 📐 Modelagem do Projeto 
<br>

O sistema foi organizado seguindo o padrão MVC (_Model-View-Controller_):

```
sistema-monitoramento-fake-news-e-qualidade-informacao/
│
├── controllers/
│   ├── __init__.py
│   └── controller_noticia.py  # Gestão da lógica e análise das notícias 
├── models/
│   └── noticia.py             # Definição do domínio e regras de validação rigorosa
└── views/
    └── interface.py           # Camada de interação e abstração do usuário
```

<br><br>
  
## 🚀 Tecnologias Utilizadas
<br>

- **Python 3.13.11** (Linguagem de Progrmação)
- **POO** (Programação Orientada a Objetos)
- **MVC** (Padrão de Arquitetura de Software)

<br><br>

## ▶️ Como executar o sistema 
<br>


**Discentes:** Bruna Eduarda, Caio Victor, Pedro Henrique, Rayssa Beatriz e Tainá Almeida.
