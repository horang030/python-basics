# 객체의 대소 비교

# a = 1
# b = 3
# print(a > 10)
# print(2 < 4)
print(1 > 3)
print(2 < 4)

print(1 >= 3)
print(3 <= 4)

print(1 == 3)
print(1 != 3)

# 복합관계식을 지원해준다
# 0 < a < 10

# 다른 언어는 지원이 안되지만 파이썬은 수학에 특화되어 지원해줌
a = 4
print(0 < a and a < 10)
print(0 < a < 10)

# 수치형 이외의 다른 타입 객체 비교
print('abcd' > 'abc')
print('aac' > 'abc')
# tuple은 바른 값들을 순서있게 있는 것을 말함
print([1, 2, 3] < [1, 2, 4])
print((1, 2, 3) < (1, 2, 4))

# 10살, '둘리', '010-0000-0000'을 따로 모아놓고 싶다고 가정한다면
# (10, '둘리', '010-0000-0000') 처럼 tuple을 사용하면 용이
# 2000, 3000,5050 은 [2000, 3000, 5050] 처럼 리스트를 써라

# 동질성  ==    (같은 객체의 값인지 비교)
# 동일성  is    (같은 개체인지 비교)
a = 20
b = 20
c = a

print(a == b)  # True
print(a is b)  # True
print(a is c)  # True
print(a == c)  # True

