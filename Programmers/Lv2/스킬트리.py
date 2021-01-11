def solution(skill, skill_trees):
    answer = 0

    for s in skill_trees:
        i = 0
        now = 0
        while i < len(s):
            if s[i] in skill:
                if s[i] == skill[now]:
                    now += 1
                else:
                    break
            i += 1
        else:
            answer += 1

    return answer