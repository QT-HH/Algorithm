def solution(n):
    res = []
    while n:
        res.append(n % 3)
        n = n // 3
    answer = res[-1]
    f = 1
    for i in range(2,len(res)+1):
        answer += f*3*res[-i]
        f*=3

    return answer

n=int(input())
print(solution(n))