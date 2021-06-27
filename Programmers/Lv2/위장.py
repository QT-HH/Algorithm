def solution(clothes):
    answer = 0

    clothes_dict = dict()
    for i in clothes:
        if clothes_dict.get(i[1]):
            clothes_dict[i[1]] += 1
        else:
            clothes_dict[i[1]] = 2

    res = 1
    for i in clothes_dict:
        res *= clothes_dict[i]

    answer = res - 1

    return answer