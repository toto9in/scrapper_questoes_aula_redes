# 📘 Scrapper para respostas da aula de redes no IFTM

Um simples scraper em Python para extrair respostas corretas de questões do site [itexamanswers.net](https://itexamanswers.net).
PURA MALVADEZA

O que faz:
- Converte a pergunta em um formato de URL válido.
- Realiza o scraping da página e extrai a resposta correta.
- Identifica múltiplas respostas corretas quando aplicável.

## **Requisitos**

Certifique-se de ter o Python instalado e as bibliotecas listadas em `requirements.txt`:

```bash
pip install -r requirements.txt
```

O projeto utiliza as seguintes principais bibliotecas:

```
requests
beautifulsoup4
```

##  **Como usar**

1. **Clone o repositório** e entre no diretório do projeto:

```bash
git clone https://github.com/toto9in/scrapper_questoes_aula_redes
cd scrapper_questoes_aula_redes
```

2. **Crie e ative um ambiente virtual :**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/MacOS
source venv/bin/activate
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Execute o script:**

```bash
python main.py
```

5. **Digite a pergunta quando solicitado:**

### **Exemplos de uso**

#### Exemplo com uma resposta correta:

```
Digite a questão: Which step of the communication process is concerned with properly identifying the address of the sender and receiver?

Resposta Correta:
 Formatting
```

#### Exemplo com múltiplas respostas corretas:

```
Digite a questão: Which two protocols are service discovery protocols? (Choose two.)

Resposta Correta:
 Mais de uma resposta correta encontrada
1 - DNS
2 - DHCP
```

#### Exemplo de URL ou questão inválida:

```
Digite a questão: Questão inexistente

Erro ao acessar a url: https://itexamanswers.net/question/questao-inexistente
Conteudo não encontrado
```

## **Observações**

- Esse script é para malvade pura. Mas culpa do site que tem um banco de questões da Cisco.
- Sei que você é um aluno vagabundo que nem eu e meus amigos e quer passar em redes da maneira mais Ez possível, então utilize!


**Feito por [toto9](https://github.com/toto9in)**

