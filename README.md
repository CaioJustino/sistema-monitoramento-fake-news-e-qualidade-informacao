# Sistema de Monitoramento de Fake News e Qualidade da Informação 

O presente trabalho buscou aplicar conceitos da disciplina de Boas Práticas de Programação (DIM0501) a fim de melhorar um sistema mal estruturado de monitoramento de fake news e qualidade da informação, sem reescrevê-lo do zero.

<br>

## 💻 Funcionalidades do Sistema 
<br>

- **Cadastrar Notícias**
  - Adicionar notícias ao repositório do projeto.  

- **Classificação das Notícias**
  - O sistema classifica as notícias como Confiável, Duvidosa ou Falsa.
  
- **Listar as Notícias**
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
│   └── controller_noticia.py  # Gestão da lógica, análise das notícias e mais regras de validação 
├── models/
│   └── noticia.py             # Definição do domínio e regras de validação
└── views/
    └── interface.py           # Camada de interação, abstração do usuário e regras de validação
└── app.py                     # Módulo responsável pela execução integrada e centralizada do sistema
└── README.md
```

<br><br>
  
## 🚀 Tecnologias Utilizadas
<br>

- **Python 3.13.11** (Linguagem de Progrmação)
- **POO** (Programação Orientada a Objetos)
- **MVC** (Padrão de Arquitetura de Software)

<br><br>

## ▶️ Como Executar o Sistema 
<br>

- **1. Clone este repositório no seu computador:**
```
git clone https://github.com/CaioJustino/sistema-monitoramento-fake-news-e-qualidade-informacao.git
```

- **2. Em seguida, acesse o diretório que foi criado na IDE da sua preferência. O nome do diretório será:**
```
sistema-monitoramento-fake-news-e-qualidade-informacao
```

- **3. Por fim, inicie a execução do sistema com o seguinte comando (execute "app" como um módulo):**
```
python -m app
```

<br><br>

**Discentes:** Bruna Eduarda, Caio Victor, Pedro Henrique, Rayssa Beatriz e Tainá Almeida.
