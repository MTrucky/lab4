# lab_4
## Вариант_2
> * Замыкание для получение текста ответа на запрос к API, например https://dogapi.dog/api/v2/facts.

> * Декоратор, ограничивающий частоту вызовов функций.
____
### Создание функции, получающей ответ с API.

используется библиотека [requests](https://pypi.org/project/requests/)
```
import requests

def create_dog_fact_fetcher():
    def get_dog_fact():
        response = requests.get('https://dogapi.dog/api/v2/facts')
        data = response.json()
        fact = data['data'][0]['attributes']['body']
        return fact
    return get_dog_fact
```
### Создание декоратора, ограничивающего кол-во вызовов до 3 за время 

Код создаёт декоратор **rate_limiter**, который ограничивает количество вызовов функции в течение 5 секунд до 3 раз. Функция **get_dog_fact** возвращает функцию **fact**, которая получает факт о собаке из API. В цикле функция **get_dog_fact** вызывается 10 раз, но из-за ограничения декоратора, факт о собаке выводится только три раза, после чего выводится сообщение "Много".
____

Результат работы:

> ![image](https://github.com/MTrucky/lab4/assets/146337304/758257ec-f893-4426-a073-88d5596a85c8)


 [Декораторы](https://habr.com/ru/companies/otus/articles/727590/)

 [Замыкания](https://habr.com/ru/companies/skillfactory/articles/542880/)
