res = []
res_dic = dict()

for i in range(10000):
    counter = 0
    for j in range(1,i+1):   
        if(i%j == 0):
            counter += 1
    if(counter == 2):
        temp = str(i)
        if(temp[-1] == "9"):
            res.append(i)
for i in range(1,101):
    res_dic[(100*i)-1] = 0 

temp = []
for key in res_dic:
    helper = []
    for i in range(len(res)):
        counter1 = 0   
        if(res[i]<=key and res[i]>=key-100+1):
            counter1 += 1
            helper.append(res[i])
    temp.append(helper)
for i in range(len(temp)):
    print(f"Number of prime numbers from {i*100} to {i*100+99} = {len(temp[i])}")
    for j in range(len(temp[i])):
        print(temp[i][j],end=' ',sep=' ')
    print()