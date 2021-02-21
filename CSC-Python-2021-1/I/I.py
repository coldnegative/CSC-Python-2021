#!/usr/bin/env python
# -*- coding: utf-8 -*-
def writer(line):
    with open("output.txt", "a") as f:
        f.write(line)


def main():
    """Дан секвенированный геном какого-либо вируса.
    Нужно определить количество нуклеотидов a c g t
    в геноме в таком порядке."""
    # Code goes over here.
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0
    with open("input.txt") as f:
        for line in f:
            for x in "".join(line[10:].split()):
                if x == "a":
                    count_a += 1
                elif x == "c":
                    count_c += 1
                elif x == "g":
                    count_g += 1
                elif x == "t":
                    count_t += 1
        else:
            writer("{} {} {} {}\n".format(count_a, count_c, count_g, count_t))
    return 0


if __name__ == "__main__":
    main()
