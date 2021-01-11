def solution(a):
    answer = 0

    visited = {}

    i = 0
    while i < len(a):
        if a[i] not in visited:
            visited[a[i]] = set()
        if 0 <= i - 1 and i - 1 not in visited[a[i]] and a[i - 1] != a[i]:
            visited[a[i]].add(i - 1)
        elif i + 1 < len(a) and a[i + 1] != a[i]:
            visited[a[i]].add(i + 1)
        i += 1

    for i in visited:
        answer = max(answer, len(visited[i]))

    return answer * 2