import re

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
    company_name = company_name_a.text
    # print(company_name)

    vacancies_info.append({
        'link': link_vacancy,
        'salary': salary,
        'city': city,
        'company_name': company_name
    })
print(vacancies_info)
# pprint(vacancies_info)
    # salary = salary_span.text
    # print(salary_span)
    #     r = re.findall(r'address>[а-яА-Я-]+', str(city))
    #     print(r)
    # cities = vacancies_links.find('div', attrs={"data-qa": "vacancy-serp__vacancy-address"})

    # for links in links_vacancy_list:
    #     link = links.find('a', href=re.compile("https:"))
    #     list_links.append(str(link))
    #     for target_link in list_links:
    #         if 'Django' in target_link:
    #             correct_list_links.append(target_link)
    # pprint(correct_list_links)

    # for link in links_vacancy_list:
    #     salary = link.find('span', attrs={"data-qa": "vacancy-serp__vacancy-compensation"})
    # print(salary)
    # r = re.findall("[от]|[до]|\d{1,10}", str(salary).strip())
    # print(r)
    #
    # for find_key_words_jango_flask in links_vacancy_list:
    #     all_links_vacancies = find_key_words_jango_flask.find('a')
    # print(all_links_vacancies)
    # for vacancies_with_key_words in all_links_vacancies:
    #     print(vacancies_with_key_words)
    #         list_of_salaries.extend(r)
    # print(list_of_salaries)
    #         r = re.findall("(\d+)", str(salary))
    #         list_of_salaries.extend(r)
    # print(list_of_salaries)
