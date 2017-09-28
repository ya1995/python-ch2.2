# 객체 값 대소 비교
print(1 > 3)
print(2 < 4)
print(4 <= 5)
print(4 >= 5)
print(6 == 9)
print(6 != 9)

# 복합관계식도 지원
a = 6
print(0 < a < 10)

# 수치형 이외의 객체도 비교가능
print('abcd' > 'abc')
print([1, 2, 4] > [1, 2, 3, 5])

# 동질(값)성 비교
# 동일(참조값)성 비교

a = 10
b = 20
c = 10

print(a == b)
print(a is b)

print(a == c)
print(a is b)