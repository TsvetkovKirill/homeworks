str = '''lastname,firstname,surname,organization,position,phone,email
Усольцев Олег Валентинович,,,ФНС,главный специалист – эксперт отдела взаимодействия с федеральными органами власти Управления налогообложения имущества и доходов физических лиц,+7 (495) 913-04-78,opendata@nalog.ru
Мартиняхин Виталий Геннадьевич,,,ФНС,,+74959130037,
Наркаев,Вячеслав Рифхатович,,ФНС,,8 495-913-0168,
Мартиняхин,Виталий,Геннадьевич,ФНС,cоветник отдела Интернет проектов Управления информационных технологий,,,
Лукина Ольга Владимировна,,,Минфин,,+7 (495) 983-36-99 доб. 2926,Olga.Lukina@minfin.ru
Паньшин Алексей Владимирович,,,Минфин,,8(495)748-49-73,1248@minfin.ru
Лагунцов Иван Алексеевич,,,Минфин,,+7 (495) 913-11-11 (доб. 0792),
Лагунцов Иван,,,,,,Ivan.Laguntcov@minfin.ru'''
changed_str = ''
fixed_book = []
for person in phone_book:
    other_fields = person[3:]
    refactored_names = ' '.join(person[:3]).split()
    while len(refactored_names) != 3:
        refactored_names.append('')
    refactored_names.extend(other_fields)
    fixed_book.append(refactored_names)
print(fixed_book)