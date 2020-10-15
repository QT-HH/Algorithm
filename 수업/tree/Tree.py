# 바이너리 트리를 배열로 표현하기
class BinaryTree:
    def __init__(self,H):
        self.tree = [-1] * (1<<(H+1))

    #부모 노드, 자식노드 정보를 가지고 insert
    def insert(self,parent,child):
        # tree 안에 부모가 없으면, 루트
        if parent not in self.tree:
            self.tree[1] = parent
            self.tree[2] = child
        else:
            p_idx = self.tree.index(parent)
            if self.tree[p_idx<<1]==-1:
                self.tree[p_idx<<1] = child
            else:
                self.tree[(p_idx<<1)+1] = child

    def print_tree(self):
        print(self.tree)

    def pre_order(self,idx):
        if idx>=len(self.tree):
            return
        if self.tree[idx]!=-1:
            print(self.tree[idx],end=" ")
            self.pre_order(idx<<1)
            self.pre_order((idx<<1)+1)

    def in_order(self,idx):
        if idx>= len(self.tree):
            return
        if self.tree[idx] != -1:
            # 왼쪽
            self.in_order(idx<<1)
            # 부모
            print(self.tree[idx],end=" ")
            # 오른쪽
            self.in_order((idx<<1)+1)

    def post_order(self,idx):
        if idx >= len(self.tree):
            return
        if self.tree[idx] !=-1:
            self.post_order(idx<<1)
            self.post_order((idx<<1)+1)
            print(self.tree[idx],end=" ")

H = 4
my_tree = BinaryTree(H)
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
edges = list(map(int,input().split()))
for i in range(0,len(edges),2):
    my_tree.insert(edges[i],edges[i+1])

my_tree.print_tree()
my_tree.pre_order(1)
print()
my_tree.in_order(1)
print()
my_tree.post_order(1)