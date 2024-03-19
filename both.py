from time import time, sleep
import requests

def dec(fun):
    timenow = time()
    calls = 0
    def checks():
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
    return checks

@dec
def get_dog_fact():
    response = requests.get('https://dogapi.dog/api/v2/facts')
    data = response.json()
    fact = data['data'][0]['attributes']['body']
    return fact


dog_fact = get_dog_fact()
print(dog_fact)
dog_fact = get_dog_fact()
print(dog_fact)
dog_fact = get_dog_fact()
print(dog_fact)
dog_fact = get_dog_fact()
print(dog_fact)
sleep(6)
dog_fact = get_dog_fact()
print(dog_fact)
dog_fact = get_dog_fact()
print(dog_fact)
dog_fact = get_dog_fact()
print(dog_fact)
dog_fact = get_dog_fact()
print(dog_fact)

# for _ in range(4):
#     dog_fact = get_dog_fact()
#     print(dog_fact)
#     sleep(1)
