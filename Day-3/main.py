import re

INPUT_FILE = 'input.txt'

def read_file(filepath: str) -> str:
    """
    Opens the file at given filepath.
    :param filepath: Path to input.txt.
    :return: File content as string.
    """
    with open(INPUT_FILE, 'r') as handle:
        return handle.read()


def get_valid_mul(corrupted_code: str) -> list:
    """
    Use regex to find all valid mul() blocks.
    :param corrupted_code: String to use regex on.
    :return: List with all valid mul() blocks.
    """
    valid_list = re.findall(r'mul\((\d+,\d+)\)', corrupted_code)
    return valid_list


def get_valid_mul_part2(corrupted_code: str) -> list:
    """
    Use regex to split string at do and don't pattern, then find all valid
    mul() blocks following a do pattern.
    :param corrupted_code: String to use regex on.
    :return: list with all valid mul() blocks for part 2.
    """
    dont_pattern = r"don't\(\)"
    do_pattern = r"do\(\)"
    mul_pattern = r'mul\((\d+,\d+)\)'

    split_parts = re.split(f"({dont_pattern}|{do_pattern})", corrupted_code)

    valid_mul = []
    enabled = True

    for part in split_parts:
        part = part.strip()
        if part == "do()":
            enabled = True
        elif part == "don't()":
            enabled = False
        elif enabled:
            matches = re.findall(mul_pattern, part)
            valid_mul.extend(matches)

    return valid_mul


def transform_str_to_int(a_list: list[str]) -> list[tuple[int,int]]:
    """
    Transforms a list with string items into a list of tuples with integer pairs.
    :param a_list: A list with string items.
    :return: List of tuples with integer pairs.
    """
    list_of_str = [item.split(',') for item in a_list]
    return [(int(item[0]), int(item[1])) for item in list_of_str]


def add_all_multiplications(list_of_int_tuple: list[tuple[int,int]]) -> int:
    """
    Iterate over given list and multiply every integer pair in each item, then add every product together.
    :param list_of_int_tuple: List of tuples with integer pairs.
    :return: The sum of all products as integer.
    """
    sum_of_multiplications = 0
    for item in list_of_int_tuple:
        sum_of_multiplications += item[0] * item[1]

    return sum_of_multiplications


def main():
    corrupted_code = read_file(INPUT_FILE)

    # solution part 1
    valid_list_str = get_valid_mul(corrupted_code)
    valid_list_with_int_tuple = transform_str_to_int(valid_list_str)
    print(add_all_multiplications(valid_list_with_int_tuple))

    #solution part 2
    valid_list_str_part2 = get_valid_mul_part2(corrupted_code)
    valid_list_with_int_tuple2 = transform_str_to_int(valid_list_str_part2)
    print(add_all_multiplications(valid_list_with_int_tuple2))


if __name__ == '__main__':
    main()