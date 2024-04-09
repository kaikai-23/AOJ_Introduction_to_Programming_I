# 標準入力、2つの整数

# map関数は、第二引数に対して第一引数の関数を適応
# スペース区切りに対してはsplitを使用する
a,b = map(int,input().split())
print(a*b, (a+b)*2)

# 別解1
# a, b = input().split()
# print(int(a) * int(b), (int(a) + int(b)) * 2)
