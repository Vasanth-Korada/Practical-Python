n = int(input())
psc_list = list(map(int,input().split()))

res = [0]

for i in range(1,n):
    count = 0
    for j in range(0,i):
        if(psc_list[j] > psc_list[i]):
            count = count + 1
    res.append(count)
print(res)

