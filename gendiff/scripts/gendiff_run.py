from gendiff import take_args, generate_diff


def main():
    first_file_path, second_file_path, formatter = take_args()
    print(generate_diff(first_file_path, second_file_path, formatter))


if __name__ == '__main__':
    main()
