# данный модуль позволяет обработать
# центральное распределение и дисперсию
# чтобы на выходе получить рандомное значение распределения Гаусса
# ф-я get_random_value вернёт случайное значение в формате json

import math
import random
import json


class Gauss_Random:
    """
        Модуль вернёт рандомное значение Гаусс распределения
        передайте среднее и дисперсию, как аргументы ф-ии   get_random_value()
        возвращаемое значение будет в json формате
    """

    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def get_random_value(self) -> str:
        return self._return_json(random.gauss(self.mu, math.pow(self.sigma, 1 / 2)))

    def _return_json(self, random_value: int) -> str:
        return json.dumps({"gauss_value": random_value})

    def __str__(self) -> str:
        return 'Gauss_Random object'

    def __repr__(self) -> str:
        return "Gauss_Random object"


print(random.gauss(5, 2))
object = Gauss_Random(5, 2)
print(object.get_random_value())
