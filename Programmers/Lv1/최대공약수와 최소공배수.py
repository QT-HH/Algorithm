def solution(n, m):
    answer = []
    big = max(n, m)
    small = min(n, m)
    for i in range(small, -1, -1):
        if not small % i and not big % i:
            answer.append(i)
            break

    i = 1
    while True:
        if not big * i % small:
            answer.append(big * i)
            break
        i += 1

    return answer