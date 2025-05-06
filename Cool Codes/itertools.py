# mine
import itertools

dishes = itertools.product(main_courses, desserts, drinks)
prices = itertools.product(price_main_courses, price_desserts, price_drinks)

for dish, price in zip(dishes, prices):
    if (total := sum(price)) <= 30:
        print(*dish, total)
