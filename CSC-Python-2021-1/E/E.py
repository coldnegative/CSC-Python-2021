#!/usr/bin/env python
# -*- coding: utf-8 -*-
def main():
    """ Напишите программу, которая преобразует строку в заголовок
    (каждое слово с большой буквы).
    Части речи не учитывать: предлоги тоже преобразуются по этому правилу. """
    # Code goes over here.
    header = list(str(input()).split())
    for i, word in enumerate(header):
        word_capitalized = word[0].capitalize() + word[1:]
        header[i] = word_capitalized
    print(" ".join(header))
    return 0


if __name__ == "__main__":
    main()
