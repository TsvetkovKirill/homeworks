import json
from pprint import pprint
with open('manager_sales.json', 'r') as file:
    list = json.load(file)
all_sum = []
sum_first_men = 0
print(list[0]['manager']['first_name'], list[0]['manager']['last_name'])
for i in list[0]['cars']:
    sum_first_men += i['price']
all_sum.append(sum_first_men)

sum_second_men = 0
print(list[1]['manager']['first_name'], list[1]['manager']['last_name'])
for i in list[1]['cars']:
    sum_second_men += i['price']
all_sum.append(sum_second_men)

sum_third_men = 0
print(list[2]['manager']['first_name'], list[2]['manager']['last_name'])
for i in list[2]['cars']:
    sum_third_men += i['price']
all_sum.append(sum_third_men)

sum_forth_men = 0
print(list[3]['manager']['first_name'], list[3]['manager']['last_name'])
for i in list[3]['cars']:
    sum_forth_men += i['price']
all_sum.append(sum_forth_men)
print(all_sum)

sum_fith_men = 0
print(list[4]['manager']['first_name'], list[4]['manager']['last_name'])
for i in list[4]['cars']:
    sum_fith_men += i['price']
all_sum.append(sum_fith_men)
print(all_sum)

sum_sixth_men = 0
print(list[5]['manager']['first_name'], list[5]['manager']['last_name'])
for i in list[5]['cars']:
    sum_sixth_men += i['price']
all_sum.append(sum_sixth_men)
print(all_sum)

sum_seventh_men = 0
print(list[6]['manager']['first_name'], list[6]['manager']['last_name'])
for i in list[6]['cars']:
    sum_seventh_men += i['price']
all_sum.append(sum_seventh_men)
print(all_sum)

sum_eight_men = 0
print(list[7]['manager']['first_name'], list[7]['manager']['last_name'])
for i in list[7]['cars']:
    sum_eight_men += i['price']
all_sum.append(sum_eight_men)
print(all_sum)

sum_nineht_men = 0
print(list[8]['manager']['first_name'], list[8]['manager']['last_name'])
for i in list[8]['cars']:
    sum_nineht_men += i['price']
all_sum.append(sum_nineht_men)
print(all_sum)

sum_ten_men = 0
print(list[9]['manager']['first_name'], list[9]['manager']['last_name'])
for i in list[9]['cars']:
    sum_ten_men += i['price']
all_sum.append(sum_ten_men)
max_value = max(all_sum)
print(max_value)