import random

r = random.randint(1, 100)
while True:
    num = input('請猜數字: ')
    num = int(num)
    if num == r:
        print('你猜中了!')
        break
    elif num > r:
        print('小一點')
    elif num < r:
        print('大一點')
    else:
        print('請輸入1-100的整數')

