"""Небольшой модуль для напоминания делать перерыв при работе за компьютером"""
import time
from plyer import notification


class EyesSaver:
    """
    Класс, который отвечает за вывод сообщения каждый 30 минут
    """

    def __init__(self):
        # 2400 = 30 минут за компьютером + 10 перерыва * 60 секунд
        self.__time_for_wait = 2400
        self.__message = "Прошло пол часа и пора размять глаза"
        self.__title = "Помни о глазах"

    def wait_time(self):
        """
        Отсчитывает 30 минут перед тем как сделать перерыв
        """
        time.sleep(self.__time_for_wait)

    def show_message(self):
        """
        Выводит уведомление о том, что надо сделать перерыв
        """
        notification.notify(message=self.__message, title=self.__title)

    def work(self):
        """
        Фасад для бесконечной работы в пассивном режиме
        """
        while True:
            self.wait_time()
            self.show_message()


if __name__ == '__main__':
    eyes_saver = EyesSaver()
    eyes_saver.work()
