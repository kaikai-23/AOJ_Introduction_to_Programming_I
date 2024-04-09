# 小数点以下6位まで表示
x, y = map(int, input().split())
print(x//y, x%y, '{:.6f}'.format(x/y))
