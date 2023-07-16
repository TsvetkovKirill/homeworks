from bs4 import BeautifulSoup
from pprint import pprint
with open('Расписание adpy-76 Профессиональная работа с Python.html', encoding='UTF-8') as file:
    src = file.read()
soup = BeautifulSoup(src, 'lxml')
result = soup.find_all('div', attrs={'data-testid':'program-lesson-title'})
links = [link.text for link in result]
pprint(links)