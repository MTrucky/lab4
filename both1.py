import requests
import time

def rate_limits(max_calls, period):
    def decorator(func):
        calls = 0
        last_reset = time.time()

        def wrapper(*args, **kwargs):
            nonlocal calls, last_reset

            # Вычисляем время, прошедшее с момента последнего сброса
            elapsed = time.time() - last_reset

            # Если прошедшее время больше периода, сбрасываем счетчик вызовов
            if elapsed > period:
                calls = 0
                last_reset = time.time()

            # Проверяем, не превышен ли лимит вызовов
            if calls >= max_calls:
                raise Exception("Rate limit exceeded. Please try again later.")

            calls += 1

            # Вызываем оригинальную функцию
            return func(*args, **kwargs)

        return wrapper
    return decorator

def create_dog_fact_fetcher():
    @rate_limits(max_calls=1, period=10) 
    def get_dog_fact():
        response = requests.get('https://dogapi.dog/api/v2/facts')
        data = response.json()
        fact = data['data'][0]['attributes']['body']
        return fact
    return get_dog_fact

# Создаем экземпляр функции get_dog_fact через замыкание
fetch_dog_fact = create_dog_fact_fetcher()

# Используем созданный экземпляр для получения и вывода факта о собаке
try:
    dog_fact = fetch_dog_fact()
    print(dog_fact)
except Exception as e:
    print(f"Error occurred: {e}")
