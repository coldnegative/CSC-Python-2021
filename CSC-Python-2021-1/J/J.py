#!/usr/bin/env python
# -*- coding: utf-8 -*-
from re import sub


def writer(line):
    with open("output.txt", "a") as f:
        f.write(line)


def main():
    """Дан текст с меню, котором указана цена в долларах (всегда целое число).
    Перевести его по курсу $1 = 75р в рубли.
    Воспользуйтесь предыдущим кодом:
    сумму в рублях делите по группам из 3 разрядов.
    В выводе буква р - это кириллица."""
    # Code goes over here.
    with open("input.txt") as f:
        for line in f:
            writer(
                sub(
                    r"\$\d+",
                    lambda m:
                    "{:,}".format(int(m.group()[1:]) * 75).replace(",", " ")
                    + "р",
                    line,
                )
            )
    return 0


if __name__ == "__main__":
    main()
