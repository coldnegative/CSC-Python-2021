#!/usr/bin/env python
# -*- coding: utf-8 -*-
def main():
    """Напишите в порядке возрастания
    все делители числа, кроме 1 и его самого."""
    # Code goes over here.
    a = int(input())
    for i in range(2, a):
        if a % i == 0:
            print(str(i) + " ", end="")
    else:
        print()
    return 0


if __name__ == "__main__":
    main()
