import re
import csv


def get_data_from_csv(path: str) -> dict:
    with open(path) as f:
        rows = csv.reader(f, delimiter=',')
        data = list(rows)
        headers = data[0]
        book = data[1:]

        return {
            'book': book,
            'headers': headers
        }


def normalize_names(phone_book: list[list[str]]) -> list[list[str]]:
    """
    Splits first three strings in each list which represents surname, name
        and last name, and rewrites them so each nested list follows
        the same pattern:
            ['surname', 'name', 'last name', ...next fields...].
    """
    fixed_book = []
    for person in phone_book:
        other_fields = person[3:]
        refactored_names = ' '.join(person[:3]).split()
        while len(refactored_names) != 3:
            refactored_names.append('')
        refactored_names.extend(other_fields)
        fixed_book.append(refactored_names)

    return fixed_book


def normalize_phones(phone_book: list[list[str]]) -> list[list[str]]:
    """
    If string with phone is not blank, uses regex to change phone number to
        '+7(999)999-99-99' and '+7(999)999-99-99 доб.9999' if additional
        4 digits is present.
    """
    telephones_search = r'(\+7|8) ?\(?(\d{3})\)?[ -]?(\d{3})[-]?(\d{2})-?(\d{2})( \(?доб. (\d{4})\)?)?'
    without_additional = r'+7(\2)\3-\4-\5'
    with_additional = r'+7(\2)\3-\4-\5 доб.\7'

    fixed_phones = phone_book.copy()
    for position, person in enumerate(phone_book):
        if person[-2] == '':
            continue
        if re.search(telephones_search, person[-2]).group(7) is None:
            number = re.sub(telephones_search, without_additional,
                            person[-2])
        else:
            number = re.sub(telephones_search, with_additional,
                            person[-2])

        fixed_phones[position][-2] = number
    return fixed_phones


def merge_duplicates(phone_book: list[list[str]]) -> list[list[str]]:
    """
    Checks if there is duplicated 'surname + name' fields and merges this
        lists together.
    """
    merged_book = {}

    for person in phone_book:
        full_name = f'{person[0]} {person[1]}'
        if merged_book.get(full_name):
            for pos, field in enumerate(person):
                if field == '':
                    continue
                merged_book[full_name][pos] = field
        else:
            merged_book[full_name] = person

    fixed_duplicates = [person for person in merged_book.values()]
    return fixed_duplicates


def write_to_csv(headers: list, data: list, path: str) -> None:
    """
    Merges headers and data into one list and writes it into csv.
    """
    headed_book = [headers.copy()] + data.copy()

    with open(path, "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(headed_book)


def main() -> None:
    phone_book = get_data_from_csv('raw.csv')
    steps = (normalize_names, normalize_phones, merge_duplicates)

    for step in steps:
        phone_book['book'] = step(phone_book['book'])

    write_to_csv(phone_book['headers'], phone_book['book'],
                 'phone_book.csv')


if __name__ == '__main__':
    main()