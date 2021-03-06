# 산술연산
# 관계연산 > < >= <= == != is
# 논리연산 not or and
# 비트연산 (컴퓨터를 이해하는데 도움이 많이 됨)
# 로직 짤 때는 관계+논리가 중요하다

print(2+3)
print(2-3)
print(2*3)
# int / int 로 하면 다른 언어는 0이 나오는게 일반적, 파이썬은 실제 나눗셈으로 처리
print(2/3)
# int / float 로 하면 다른 언어는 float가 되고
print(2/3.0)
print(2.0/3)
print(2.0/3.0)

print(2//3)
print(2**3)
print(2%3)
print(divmod(2,3))

# //(몫연산), **(지수승), %(나머지 연산)
# 지수함수랑 로그함수를 알아야 함 (다음주)

# div = 나눈다, mod = 나머지 의미
# divmod() 함수 (객체없이 쓸 수 있다.)
t = divmod(2, 3)
print(t, type(t))
a, b = divmod(2, 3)
print(a, b)

# y=f(x)
# 파이썬이 가지고 있는 장점 원패킹
# 반환값

# 연산자 우선
# - 단항연산자
# * / + - 이항연산자

# 우선순위
# 1. - (minus를 붙이는 거라 피연산자가 1개 필요)
# 2. * / 순서
# 3. + - (빼기는 피연산자가 2개 필요)
print(2 + 3 * 4)
print(-2 + 3 * 4)
print(-(2 + 3) * 4)


# 결합순서
# 1. -> : + - * /
# 2. <- : + (부호) -(부호), **
print(2 ** 3 ** 4)
print((2 ** 3) ** 4)
print(2 ** (3 ** 4))
