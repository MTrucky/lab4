from time import time, sleep

def dec(fun):
    timenow = time()
    calls=0
    def checks():
        nonlocal timenow
        nonlocal calls
        if time()-timenow>5:
            timenow=time()
            calls=0
        calls+=1
        if calls<=2:
            fun()
        else:
            print("Много")
    return checks
    
@dec
def func():
    print("колл")

func()
func()
func()
func()
sleep(7)
func()
func()
func()
func()
sleep(7)
func()
