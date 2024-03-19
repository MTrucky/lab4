from time import time, sleep
import requests

def rate_limiter(fun):
    timenow = time()
    calls = 0

    def wrapper():
        nonlocal timenow, calls
        if time() - timenow > 5:
            timenow = time()
            calls = 0
        calls += 1
        if calls <= 3:
            return fun()
        else:
            print("Много")
            return None # Return None or appropriate value when rate limit is exceeded

    return wrapper

def get_dog_fact_closure():
    last_fact = None

    def get_dog_fact():
        nonlocal last_fact
        if last_fact is None:
            response = requests.get('https://dogapi.dog/api/v2/facts')
            data = response.json()
            fact = data['data'][0]['attributes']['body']
            last_fact = {'fact': fact}
        return last_fact['fact']

    return get_dog_fact

# Create an instance of the closure
dog_fact = get_dog_fact_closure()

for _ in range(30):
    print(dog_fact())
    sleep(1) # Sleep to simulate waiting between calls

sleep(6)
print(dog_fact())
print(dog_fact())
print(dog_fact())
print(dog_fact())
print(dog_fact())
