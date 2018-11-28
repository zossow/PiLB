import threading
import time
import random


class Filozofowie(threading.Thread):
    running = True
    def __init__(self, name, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork


    def run(self):
        while (self.running):
            time.sleep(random.uniform(1, 10))
            print("%s myśli" % self.name)
            self.try_to_eat()

    def try_to_eat(self):
        while self.running:
            self.left_fork.acquire(True)
            locked = self.right_fork.acquire(False)
            if locked:
                break
            #self.left_fork.release() # odkomentuj, żeby usunąć deadlock
        else:
            return

        print("%s ma dwa widelce i je " % self.name)
        time.sleep(random.uniform(1, 10))
        print("%s już zjadł" % self.name)
        self.right_fork.release()
        self.left_fork.release()  # zwalniam ten watek

forks = [threading.Lock() for n in range(5)] #przydzielanie zasobow
philosopherNames = ('Pierwszy', 'Drugi', 'Trzeci', 'Czwarty', 'Piąty')

filo = [Filozofowie(philosopherNames[i], forks[i % 5], forks[(i + 1) % 5]) 
                for i in range(5)]

for p in filo:
    p.start()
