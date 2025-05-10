# mine
from enum import Enum

class Temperature(Enum):
    FREEZING = -6
    COLD = 10
    MODERATE = 25
    WARM = 35
    HOT = float('inf')

def get_temperature(t):
    for temp in Temperature:
        if t <= temp.value:
            return temp.name

print(get_temperature(int(input())))
# other
from enum import Enum

class Temperature(Enum):
    FREEZING = -10
    COLD = 0
    MODERATE = 20
    WARM = 30
    HOT = 40

def get_temperature(t):
    match t:
        case _ if t < -5:
            return Temperature.FREEZING.name
        case _ if -5 <= t <= 10:
            return Temperature.COLD.name
        case _ if 11 <= t <= 25:
            return Temperature.MODERATE.name
        case _ if 26 <= t <= 35:
            return Temperature.WARM.name
        case _ if t > 35:
            return Temperature.HOT.name

print(get_temperature(int(input())))
