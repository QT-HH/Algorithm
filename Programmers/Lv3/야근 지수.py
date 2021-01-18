def solution(n, works):
    answer = 0

    cnt = 0
    li = [0] * 50001
    for i in works:
        li[i] += 1
        cnt += i

    if cnt > n:
        for i in range(50000, -1, -1):
            if li[i] and n:
                if n >= li[i]:
                    li[i - 1] += li[i]
                    n -= li[i]
                    li[i] = 0
                else:
                    li[i - 1] += n
                    li[i] -= n
                    n = 0
                    break

        for i in range(50001):
            if li[i]:
                answer += i * i * li[i]

    return answer