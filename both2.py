import requests
import time
import threading
from functools import wraps

def rate_limited(max_per_second):
    """
    Декоратор, ограничивающий частоту вызовов функции.
    """
    lock = threading.Lock()
    min_interval = 1.0 / float(max_per_second)

    def decorate(func):
        last_time_called = [0.0]

        @wraps(func)
        def rate_limited_function(*args, **kwargs):
            lock.acquire()
            elapsed = time.time() - last_time_called[0]
            left_to_wait = min_interval - elapsed

            if left_to_wait > 0:
                time.sleep(left_to_wait)

            lock.release()

            ret = func(*args, **kwargs)
            last_time_called[0] = time.time()
            return ret

        return rate_limited_function

    return decorate

def create_dog_fact_fetcher():
    @rate_limited(2) # Ограничиваем вызовы до 2 в секунду
    def get_dog_fact():
        response = requests.get('https://dogapi.dog/api/v2/facts')
        data = response.json()
        fact = data['data'][0]['attributes']['body']
        return fact
    return get_dog_fact

# Создаем экземпляр функции get_dog_fact через замыкание
fetch_dog_fact = create_dog_fact_fetcher()

# Используем созданный экземпляр для получения и вывода факта о собаке
dog_fact = fetch_dog_fact()
print(dog_fact)
