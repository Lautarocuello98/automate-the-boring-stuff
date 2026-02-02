import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    flips = []

    for i in range(100):
        flips.append(random.choice(['H', 'T']))

    for i in range(len(flips) - 5):
        if flips[i] == flips[i + 1] == flips[i + 2] == flips[i + 3] == flips[i + 4] == flips[i + 5]:
            numberOfStreaks += 1

print('Número total de rachas de 6:', numberOfStreaks)
print('Rachas promedio por experimento:', numberOfStreaks / 10000)
