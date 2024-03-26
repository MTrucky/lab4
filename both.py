from time import time, sleep
import requests

def rate_limiter(fun):
    timenow = time()
    calls = 0

    def decorator():
        nonlocal timenow
        nonlocal calls

        def wrapper():
            nonlocal timenow
            nonlocal calls
            if time() - timenow > 5:
                timenow = time()
                calls = 0
            calls += 1
            if calls <= 3:
                return fun()
            else:
                print("Много")
        return wrapper
    return decorator

@rate_limiter
def get_dog_fact():
    last_fact = None

    def fact():
        nonlocal last_fact
        
        response = requests.get('https://dogapi.dog/api/v2/facts')
        data = response.json()
        fact = data['data'][0]['attributes']['body']
        last_fact = {'fact': fact}
        return last_fact['fact']

    return fact

for _ in range(30):
    dog_fact = get_dog_fact()
    print(dog_fact())
    # sleep(1)
# print(dog_fact())

