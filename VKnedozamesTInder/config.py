user_token = ''  # токен пользователя
access_token = 'vk1.a.sCvgEJuRjm2oifgRkpMKruHQVf9d-J9-rhvita4lzGHtIeAzqNLkzJgezHcaVzftMso-2ZBmIk4In2It8cXNWf_CoNGO3DNhw07wHat7D0ZYqxizRsBRrWKx0PiGCNL8ynbLuAPd_PvzURnoQY7feLuMGjyhLrfLgup6uRqWf6TLmII3czTWx1x9O3b3WEeLaQB-9F2hAWfPVEasuegf3A'
bot_key = 'iRJ19lhKFloxEH3RS7rs'
# service_key_access = '1b1f81ca1b1f81ca1b1f81caec180b563d11b1f1b1f81ca7fb869370890bfe2f63e8eec'

offset = 0  # сдвиг
line = range(0, 1000)  # последовательность для перебора найденных пользователей
host = '127.0.0.1'
user = 'postgres'
password = '0000'
db_name = 'bot_users'
link_get_token = 'https://oauth.vk.com/authorize?client_id=51697655&group_ids=221487535&display=page&redirect_uri=https://vk.com/away.php?to=https://oauth.vk.com/blank.html&scope=397317&response_type=token&v=5.131'

'''ПОЛУЧИТЬ БИТОВУЮ МАСКУ'''
stories	=   (1 << 0)	#Доступ к историям.
photos	=   (1 << 2)	#Доступ к фотографиям.
app_widget	=   (1 << 6)	#Доступ к виджетам приложений сообществ. Это право можно запросить с помощью события VKWebAppGetCommunityToken библиотеки VK Bridge.
messages	=   (1 << 12)	#Доступ к сообщениям сообщества.
docs	=   (1 << 17)	#Доступ к документам.
manage	=  (1 << 18)	#Доступ к администрированию сообщества.
print(stories | photos| messages| docs| manage)
# # phone_number	=  (1 << 287)
# print(notify| photos|status|offline)
# # print(65536 & (1 << 2))
