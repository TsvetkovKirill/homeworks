import json
with open(r'/Classes/f.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
print(data)