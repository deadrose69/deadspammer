import time
a = 1000

while a > 7:
    time.sleep(0.05)
    a -= 7
    print(f'{a+7} - 7 = {a}')
print('Я гуль')