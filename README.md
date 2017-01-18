# Ближайшие бары

Скрипт принимает на вход путь к файлу данных и выводит самый большой и самый маленький бары.
Проси ввести координаты для определения ближайшего бара. Расстояние до ближайшего бара рассчитывается как длина отрезка между введенными координатами и координатами бара.
Файл данных о барах Москвы в формате JSON можно скачать на странице [http://data.mos.ru/opendata/7710881420-bary](http://data.mos.ru/opendata/7710881420-bary)

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5 и наличия файла с данными о барах

Запуск на Linux:

```#!bash

$ python bars.py </путь/к/файлу/данных.json># possibly requires call of python3 executive instead of just python                                                                                                                                                   
# 450
# 0
# 55
# 66
# Таверна

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
