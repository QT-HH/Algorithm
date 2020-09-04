N = 4
T = 2 # 원하는 조합의 요소 개수
selected = [0]*N

def comb(selected,idx,cnt):
    if cnt == T:
        print(selected)
        return
        # 내가 원하는 개수만큼의 요소를 선택했음
    if idx >=N:
        return

    selected[idx] = 1
    comb(selected,idx+1,cnt+1)
    selected[idx] = 0
    comb(selected,idx+1,cnt)
    return

comb(selected,0,0)

