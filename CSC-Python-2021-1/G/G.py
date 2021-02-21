#!/usr/bin/env python
# -*- coding: utf-8 -*-
def writer(line):
    with open("output.txt", "a") as f:
        f.write(line)


def main():
    """Дан чек, в котором перечислены купленные товары.
    В каждой второй строке — целочисленная стоимость товара.
    Вычислите полную сумму покупки."""
    # Code goes over here.
    with open("input.txt") as f:
        total = sum(int(price) for i, price in enumerate(f, 1) if i % 2 == 0)
    writer(str(total) + "\n")
    return 0


if __name__ == "__main__":
    main()
