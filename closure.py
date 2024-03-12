import requests

def create_dog_fact_fetcher():
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
