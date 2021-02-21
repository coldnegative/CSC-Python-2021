#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import cycle


def main():
    """Закрутите спираль из чисел заданного размера.
    Под каждое число отводится на 1 позицию больше,
    чем под максимальное число в спирали.
    Закручивание идет по часовой стрелке,
    начиная с поворота направо.
    В спирали участвуют числа от 1 до n ** 2.
    Целое n на входе принадлежит отрезку [2, 20]."""
    # Code goes over here.
    n = 0
    while n not in range(2, 21):
        n = int(input())
    matrix = [[0 for i in range(n)] for j in range(n)]
    moves = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])
    check = next(moves)
    move, check = check, next(moves)
    i, j = round(n / 2), round(n / 2)
    k = 1
    for k in range(1, n ** 2 + 1):
        matrix[i][j] = f"{k:>3}"
        i, j = i + move[0], j + move[1]
        if (i + check[0], j + check[1]) not in matrix:
            move, check = check, next(moves)
    for i in range(0, n):
        print(" ".join(str(matrix[i])))
    return 0


if __name__ == "__main__":
    main()
