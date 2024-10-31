from threading import Thread, Lock
from time import sleep

total_enemies = 100
lock = Lock()

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        global total_enemies

        with lock:
            print(f"{self.name}, на нас напали!")

        while True:
            with lock:

                if total_enemies <= 0:
                    break

                total_enemies = max(0, total_enemies - self.power)
                remaining_enemies = total_enemies
                self.days += 1

                print(f"{self.name} сражается {self.days} день(дня)..., осталось {remaining_enemies} воинов.")

            sleep(1)

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")

first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")

