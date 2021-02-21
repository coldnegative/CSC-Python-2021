#!/usr/bin/env python
# -*- coding: utf-8 -*-
def main():
    """ Для целого числа, если в нем больше трех разрядов,
    используйте пробел, чтобы сгруппировать разряды по 3. """
    # Code goes over here.
    print("{:,}".format(int(input())).replace(',', ' '))
    return 0


if __name__ == "__main__":
    main()
