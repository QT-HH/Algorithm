def solution(numbers):
    x = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            x.add(numbers[i] + numbers[j])

    answer = sorted(list(x))

    return answer