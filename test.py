for test_case in range(1, 2):
    n= input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    idx = []
    total_m = []
    for j in range(100):
        moves = 0
        if ladder[0][j] == 1:
            idx.append(j)
            i = 0
            while(i<99) :
                while j<99 and ladder[i][j+1]:
                    j+=1
                    moves+=1
                else:
                    i+=1
                    moves+=1
                while j>0 and ladder[i][j-1]:
                    j-=1
                    moves+=1
                else:
                    i+=1
                    moves+=1
                if i == 99: break
                i+=1
                moves+=1
            total_m.append(moves)
    print(f'#{test_case} {idx[total_m.index(min(total_m))]}')
