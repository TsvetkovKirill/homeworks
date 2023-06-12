int = int(input())
#получить число, ввести строки, количество которых равно числу, превратить строки в списки, объединить списки в один список списков
#во второй функции объединить в один список и отсортировать по возрастанию
def quick_merge(int):
    lst_ = []
    full_lst = []
    for i in range(int):
        str_ = input()
        lst_ = str_.split()
        full_lst.append(lst_)
    return full_lst

def get_sorted_list(quick_merge):
    extend_list = []
    for i in quick_merge:
        extend_list.extend(i)
    sorted_list = sorted(extend_list)
    return sorted_list
print(get_sorted_list(quick_merge(int)))
