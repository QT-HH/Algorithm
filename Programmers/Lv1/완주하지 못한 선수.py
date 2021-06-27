def solution(participant, completion):
    par = dict()
    for i in participant:
        if par.get(i):
            par[i] += 1
        else:
            par[i] = 1

    for j in completion:
        par[j] -= 1

    for k in par:
        if par[k]:
            answer = k
            break

    return answer