import math
sqrt_25 = math.sqrt(25)
pi_value = math.pi
cos_45 = math.cos(math.radians(45))
results = [
    f"Квадратный корень из 25: {sqrt_25}",
    f"Значение числа π: {pi_value}",
    f"Косинус угла 45 градусов: {cos_45}"
]

with open("results.txt", "w") as file:
    for result in results: