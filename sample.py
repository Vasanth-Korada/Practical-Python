def minimumBribes(q):
    n = len(q)
    initialState = []
    bribe_org = {}
    counter = 0
    for i in range(1,n+1):
        initialState.append(i)
        bribe_org[i] = 0
    i = len(q)-1
    j = len(initialState)-1
    while(i>=0):
            if(q[i] == initialState[j]):
                i = i - 1
                j = j - 1
            elif(q[i] == initialState[j-1]):
                bribe_org[j] += 1
                if(bribe_org[j] > 2):
                    return(0)
                else:        
                    temp = initialState[j]
                    initialState[j] = initialState[j-1]
                    initialState[j-1] = temp
                    counter = counter + 1
                    i = i - 1
                    j = j -1
    return(counter)

print(minimumBribes([2,5,1,3,4]))
