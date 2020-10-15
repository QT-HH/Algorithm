def solution(arr):
    answer = [0, 0]
    n = len(arr)
    stack = [[0,0,n,n]]

    while stack:
        si,sj,ei,ej = stack.pop()
        a = arr[si][sj]
        if ei-si == 1:
            answer[a]+=1
            continue

        check = True
        for i in range(si, ei):
            for j in range(sj, ej):
                if arr[i][j] != a:
                    stack.append([si, sj,(si+ei) // 2, (sj+ej) // 2])
                    stack.append([si, (sj+ej) // 2, (si+ei) // 2, ej])
                    stack.append([(si+ei) // 2, sj, ei, (sj+ej) // 2])
                    stack.append([(si+ei) // 2, (sj+ej) // 2, ei, ej])
                    check = False
                    break
            if not check:
                break
        else:
            answer[a]+=1

    return answer

arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
print(solution(arr))