# lab_4
## Вариант_2
 > Замыкание для получение текста ответа на запрос к API, например https://dogapi.dog/api/v2/facts.

 > Декоратор, ограничивающий частоту вызовов функций.
____
Создание функции, получающей ответ с API.

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
