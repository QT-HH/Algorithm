import itertools


def solution(info, query):
    answer = []
    data = []
    check = {}
    check_score = {}
    x = ['cpp', 'java', 'python', 'backend', 'frontend', 'junior', 'senior', 'chicken', 'pizza']
    for i in range(1, 100001):
        check_score[i] = 0

    for i in x:
        check[i] = set()

    cnt = 0
    for i in info:
        d = i.split()
        data.append(d)
        for j in range(4):
            check[d[j]].add(cnt)
        check_score[int(d[4])] += 1
        cnt += 1

    for i in range(1, 10000):
        check_score[i + 1] += check_score[i]

    print(check_score)

    case = {}
    for i in query:
        tmp = []
        x = i.split(' and ')
        x.extend(x.pop().split())
        res = set(range(len(info)))
        for j in range(len(x) - 1):
            if x[j] == '-':
                continue
            else:
                tmp.append(x[j])
                if case.get(tuple(tmp)):
                    res = set(case[tuple(tmp)])
                else:
                    res &= check[x[j]]
                    case[tuple(tmp)] = set(res)
        else:
            answer.append(check_score[x[-1]])

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info,query))