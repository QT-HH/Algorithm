class Node():   # 연결리스트에서 하나의 요소를 저장할 객체를 만드는 클래스
    # 데이터 하나를 저장할 공간(변수)
    # 다음 노드의 주소를 저장할 변수
    def __init__(self,d):
        self.d = d
        self.next = None #다음 노드 가리키는 변수, 다음 노드 모르니 변수만 생성

    def set_next(self,next):
        self.next = next

class LinekdList():
    #노드들이 연결되어 있는 리스트
    # 데이터를 저장하는 모든 노드들을 저장하지 않음
    # 가장 앞쪽에 있는 노드(head)만을 가지고 있는다.
    # size
    def __init__(self):
        # variable annotation
        self.head: Node # head 라는 변수의 타입을 미리 지정
        self.head = None
        self.size = 0

    #삽입, 삭제, 조회, pop
    def append(self,data):  # 마지막에 노드 추가
        #마지막 노드에 새로운 노드를 만들어서 연결
        new_node = Node(data)
        current = self.head #가지고 있는게 head밖에 없음
        if current == None: # 데이터가 없음!
            self.head = new_node
        else:
            #아니면 마지막 노드를 찾아서 마지막 노드의 next에
            #새로운 노드를 연결해주면 된다.
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    def get_size(self):
        return self.size

    def delete(self,idx):   # 해당인덱스 데이터 삭제
        pass
    def get(self,idx):  # 해당인덱스 데이터 조회
        current = self.head
        for i in range(idx):
            current = current.next
        return current.d

    def pop(self): # 마지막 노드 삭제/반환
        pass

my_list = LinekdList()
my_list.append("a")
my_list.append("b")
my_list.append("c")
my_list.append("d")
my_list.append("d")
my_list.append("d")

for i in range(my_list.get_size()):
    print(my_list.get(i), end=" ")
