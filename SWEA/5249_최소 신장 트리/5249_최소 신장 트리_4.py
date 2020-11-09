import sys
sys.stdin = open('input.txt')

# 최소 신장 트리의 가중치의 합 구하기
def prim(adj, start):
    INF = float('inf')
    # 정점을 선택하기 위한 가중치를 저장하는 배열
    st = [0] * V    #출발 정점
    weight = [INF] * V
    # 각 정점이 mst에 포함되었는지 표시하는 배열
    # 각 정점이 mst에 포함되지 않았으면 0, 포함되었으면 1
    mst = [0] * V
    weight[start] = 0
    # 가중치의 합을 구하기 위한 변수
    result = 0
    # mst에 모든 정점이 선택 될 때 까지 반복
    # 정점의 개수만큼 반복문을 돌면서 정점을 선택
    for _ in range(V):
        # 현재 갈 수 있는 경로중 가장 가중치가 작은 경로를 선택
        min_w = INF
        min_v = 0
        for i in range(V):
            # 정점이 mst에 포함되지 않으면서, 가중치가 가장 작아야 함
            if mst[i] == 0 and weight[i] < min_w:
                min_w = weight[i]
                min_v = i

        # 갈 수 있는 경로 중 가중치가 가장 작은 경로가 선택됨
        mst[min_v] = 1
        result += min_w  # 선택되었으니 가중치 더하기

        # 새로 선택한 정점으로 부터 갈 수 있는 경로를 살펴보고
        # 노드를 선택하기 위한 정점의 가중치가 작아지면, 수정
        for i in range(V):
            if adj[min_v][i] > 0 and not mst[i] and adj[min_v][i] < weight[i]:
                weight[i] = adj[min_v][i]    # 특정 노드로 부터 i노드로 가는 비용최소
                st[i] = min_v

    return result

T = int(input())
for t in range(1,T+1):
    V, E = map(int,input().split())
    # V+=1
    adj = [[0]*V for _ in range(V)]
    for i in range(E):
        s,e,w = map(int,input().split())
        adj[s][e] = w
        adj[e][s] = w

    # for row in adj:
    #     print(row)
    result = prim(adj,0)
    print('#{} {}'.format(t,result))
