#!/usr/bin/env python
# -*- coding: utf-8 -*-
def main():
    """Для того, чтобы сделать на сайте «звонибельную» ссылку,
    надо указать параметр href c префиксом tel:
    Например, <a href="tel:+79012342452">+79012342452</a>
    Напишите программу, которая «оборачивает» телефон в такие теги."""
    # Code goes over here.
    tel = input()
    print('<a href="tel:%s">%s</a>' % (tel, tel))
    return 0


if __name__ == "__main__":
    main()
