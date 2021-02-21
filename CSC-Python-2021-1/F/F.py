#!/usr/bin/env python
# -*- coding: utf-8 -*-
def writer(line):
    with open("output.txt", "a") as f:
        f.write(line)


def main():
    """На вход подается текст, состоящий из строк (символ-разделитель: \n).
    Пронумеруйте строки, отдав под номер 4 символа.
    В качестве заполнителя используйте пробелы."""
    # Code goes over here.
    with open("input.txt") as input:
        for i, line in enumerate(input, 1):
            n_line = "{:>4} ".format(i) + line
            writer(n_line)
    return 0


if __name__ == "__main__":
    main()
