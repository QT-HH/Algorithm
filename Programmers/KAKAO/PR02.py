def solution(info, query):
    answer = []
    data = []
    for i in info:
        data.append(i.split())

    for i in range(len(query)):
        query[i] = query[i].split()
        tmp1 = data[:]
        cnt = 0
        for j in query[i]:
            tmp2 = []
            if j == 'and':
                continue
            elif j == '-':
                cnt += 1
                continue
            else:
                if cnt == 4:
                    for a in tmp1:
                        if int(a[cnt]) >= int(j):
                            tmp2.append(a)
                else:
                    for a in tmp1:
                        if a[cnt] == j:
                            tmp2.append(a)
            tmp1 = tmp2[:]
            cnt += 1
        answer.append(len(tmp1))

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info,query))
a = ' a s d f '
a.split