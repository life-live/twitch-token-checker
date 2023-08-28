# Twitch Token Checker

Twitch Token Checker - это скрипт на Python, который позволяет проверять валидность токенов Twitch, используя асинхронные запросы к [API] Twitch. Скрипт читает токены из файла, указанного пользователем, и записывает валидные токены в другой файл с текущей датой и временем в названии. Скрипт также выводит информацию о количестве проверенных и валидных токенов, а также время, затраченное на проверку.

## Требования

Для работы скрипта необходимо установить Python 3.7 или выше, а также библиотеки asyncio и aiohttp. Для установки библиотек можно использовать файл requirements.txt, который находится в репозитории с кодом. Для установки библиотек из файла можно выполнить команду:

```bash
pip install -r requirements.txt
```

## Использование

Для запуска скрипта можно выполнить команду:

```bash
python twitch_token_checker.py
```

Скрипт попросит ввести путь к файлу с токенами Twitch, которые нужно проверить. Файл должен содержать один токен на строку. После ввода пути к файлу скрипт начнет проверку токенов и выведет результаты на экран. Валидные токены будут записаны в файл с названием в формате "HH.MM.SS MM-DD-YYYY.txt", где HH - часы, MM - минуты, SS - секунды, DD - день, MM - месяц, YYYY - год.

Пример вывода скрипта:

```
Enter the path to the file with the Twitch tokens: tokens.txt
INFO:root:crfq2av88lasx5uizjhts2vmgd5tla is not valid
INFO:root:ceei9nmhiya90x53v5d5vp393ahcsa is valid
INFO:root:ivmj68qatwh4q08wt9tte8mhbe5br1 is not valid
INFO:root:Valid Tokens: 1/3
INFO:root:Checking 3 tokens took 0.03 seconds
```

Пример содержимого файла с валидными токенами:

```
ceei9nmhiya90x53v5d5vp393ahcsa
```
