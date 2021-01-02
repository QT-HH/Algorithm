import time
start = time.time()
cnt = 0
for i in range(100000000):
    cnt +=1

print("time :", time.time() - start)