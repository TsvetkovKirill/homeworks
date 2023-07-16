import re


def get_domain_name(url):
    pattern = re.compile(r"[\.\/][\w-]+")
    result = pattern.findall(url)
    print(result)
    if result[0] == '/www':
        return result[1][1:]
    else:
        return result[0][1:]
print(get_domain_name("www.xakep.ru"))
