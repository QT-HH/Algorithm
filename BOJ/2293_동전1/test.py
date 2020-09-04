import time
start = time.time()
total = 0
for i in range(1<<31):
    total+=1

print(total, "time: ", time.time() - start)