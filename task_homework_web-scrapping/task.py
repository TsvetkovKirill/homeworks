import re
import json
import requests
import fake_headers
import bs4
from pprint import pprint

headers = fake_headers.Headers(browser='firefox',
                               os='win')  # создали фейковые мета-данные для запроса, выдаем себя за человека
headers_data = headers.generate()  # сгенерировали их в словарь

main_html = requests.get('https://hh.ru/search/vacancy?area=1&area=2&search_field=description&search_field=name&enable_snippets=false&text=Django%2C+flask.+python&ored_clusters=true&page=0',
                         headers=headers_data).text  # направили запрос на сайт
main_soup = bs4.BeautifulSoup(main_html, 'lxml')  # парсим с помощью BS4
vacancies_info = []
all_vacancies = main_soup.find_all('div', class_='vacancy-serp-item-body__main-info')  # находим все вакансии и помещаем
# в список посредством метода find_all, итерируемся сразу по всей html
for vacancy_div in all_vacancies:
    link_vacancy = vacancy_div.find('a')['href']
    # print(link_vacancy)

    address_div = vacancy_div.find('div', attrs={"data-qa": "vacancy-serp__vacancy-address"})
    address = address_div.text
    city = address.split(',')[0]
    # print(city)

    salary_span = vacancy_div.find('span', attrs={"data-qa": "vacancy-serp__vacancy-compensation"})
    # print(salary_span)
    if type(salary_span) == bs4.element.Tag:
        salary = salary_span.text
        # print(salary)
    else:
        salary = 'No known salary'

    company_name_a = vacancy_div.find('a', attrs={"data-qa": "vacancy-serp__vacancy-employer"})
    # company_name = company_name_a.text
    if type(company_name_a) == bs4.element.Tag:
        company_name = company_name_a.text
        # print(company_name)
    else:
        company_name = 'the company name is not listed'
        # print(company_name)

    vacancies_info.append({
        'link': link_vacancy,
        'salary': ' '.join(salary.split()),
        'city': city,
        'company_name': ' '.join(company_name.split())
    })

with open("task_scrapping.json", "w", encoding='UTF-8') as file:
    json.dump(vacancies_info, file, ensure_ascii=False, indent=2)

pprint(vacancies_info)

