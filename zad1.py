# !/usr/bin/env python3
# -*- coding: utf-8 -*-from datetime import date
# Написать программу, которая считывает текст из файла и выводит на экран только цитаты,
# то есть предложения, заключенные в кавычки.

import re

if __name__ == '__main__':
    with open('lol.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    sentences = text.split('.')

    # Вывод предложений с запятыми.
    for sentence in sentences:
        if '"' in sentence:
            string = sentence
            print(re.findall(r'"(.*?)"', string))