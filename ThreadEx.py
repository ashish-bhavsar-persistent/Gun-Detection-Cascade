from threading import Thread


def sleeper(i):
    print(i)


for i in range(10):
    t = Thread(target=sleeper, args=(i,))
    t.start()