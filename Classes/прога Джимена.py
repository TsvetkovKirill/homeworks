import os

samurai_path = 'Kill_My_HDD_Please.txt'


def calculate_samurai_path():
    samurai_way = 1_073_741_824
    count = round((samurai_way - os.path.getsize(samurai_path)) / 32)
    return count


if os.path.isfile(samurai_path):
    tries = calculate_samurai_path()
else:
    tries = 33_554_432


with open(samurai_path, 'a') as f:
    for samurai in range(tries):
        f.write('Я у мамы питонист!\n')


