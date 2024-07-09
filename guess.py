import random
start = int(input('請決定隨機數字範圍開始值: '))
end = int(input('請決定隨機數字範圍結束值: '))
r = random.randint(start, end)
count = 0
while True:
    count += 1
    num = input('請猜數字: ')
    num = int(num)
    if num == r:
        print('你猜中了!,總共猜了', count, '次')
        break
    elif num > r:
        print('小一點')
    elif num < r:
        print('大一點')
    else:
        print('請輸入1-100的整數')
