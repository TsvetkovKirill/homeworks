import json

with open(r'C:\Users\29\PycharmProjects\homeworksPython\open_read_and_write_in_files\new.json', 'r', encoding='utf-8') as f:
    str_ = json.load(f)
print(type(str_))

data = '{"president": {"name": "Joe Biden", "species": "homo"}}'
d = json.loads(data)
print(type(d))
