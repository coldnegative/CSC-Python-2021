#!/usr/bin/env python
# -*- coding: utf-8 -*-
from re import sub


def writer(line):
    with open("output.txt", "a") as f:
        f.write(line)


def main():
    """Замените в тексте знаки дюйма на парные кавычки-елочки.
    Кавычки в тексте всегда парные, вложенных кавычек нет."""
    # Code goes over here.
    with open("input.txt") as f:
        for line in f:
            writer(
                sub(
                    r"(\"(.*?)\")",
                    lambda m:
                    "«" + str(m.group()[1:-1]) + "»",
                    line
                )
            )
    return 0


if __name__ == "__main__":
    main()
