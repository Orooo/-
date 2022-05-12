# https://www.youtube.com/watch?v=qojmdTg0du4&t=7s
# k 진수에서 소수의
# 개수 구하기
import math

# 소수 인지 빠르게 판별


def check(num):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False

    return True

# base 진법으로 변환


def convert(num, base):
    q, r = divmod(num, base)
    if q:
        return convert(q, base) + str(r)
    else:
        return str(r)


def solution(n, k):
    numstr = str(n) if k == 10 else convert(n, k)
    nums = numstr.split('0')

    answer = 0
    for value in nums:
        # 빈 문자열("") 아니고 소수이면 카운팅
        if len(value) and check(int(value)):
            answer += 1

    return answer


print(solution(437674, 3))
# result 3

# print(solution(110011, 10))
# # result 2
