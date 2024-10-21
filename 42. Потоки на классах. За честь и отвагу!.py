import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0
        self.victory = False

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            time.sleep(1)  # Задержка 1 секунда (1 день)
            self.days += 1
            self.enemies -= self.power
            if self.enemies < 0:
                self.enemies = 0
            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")

        self.victory = True
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание классов
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание окончания битвы
first_knight.join()
second_knight.join()

print("Все битвы закончились!")
