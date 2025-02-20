import requests
from bs4 import BeautifulSoup
import re

BASE_URL = "https://itexamanswers.net/question/"


def format_question_to_url(question):
    question = question.replace('/', "-")
    formatted = re.sub(r'[^a-zA-Z0-9\s-]', '', question)
    formatted = re.sub(r'\s+', '-', formatted.strip())
    return formatted.lower()

def scrape_question_content(question):
    formatted_question = format_question_to_url(question)
    url = BASE_URL + formatted_question
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Erro ao acessar a url: {url}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    content_div = soup.find('div', class_='dwqa-question-content')

    if content_div:
        correct_answer = content_div.find_all('li', class_='correct_answer') ## find_all retorna SEMPRE uma lista de acordo com a docs e stackoverflow
        if correct_answer == []:
            correct_answer = content_div.find_all('span', attrs={'style': 'color: #ff0000;'})


        if correct_answer.__len__() == 1:
            correct_text = correct_answer[0].text
            return correct_text
        elif correct_answer.__len__() > 1:
            correct_text = 'Mais de uma resposta correta encontrada\n'
            for i, answer in enumerate(correct_answer):
                correct_text += f"{i+1} - {answer.text}\n"
            return correct_text
    else:
        print("Conteudo da questao não encontrado")
        return None

if __name__ == "__main__":
    question = input("Digite a questão: ")

    content = scrape_question_content(question)
    if content:
        print("\nResposta Correta:\n", content)
    else:
        print("Conteudo não encontrado")