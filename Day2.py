no_of_rows = int(input("Enter Number of Steps:"))
k=0
for i in range(1,no_of_rows+1):
    for space in range(1,(no_of_rows-i)+1):
        print(end="")
    while k!=(2*i-1):
        print("*",end="")
        k=k+1
    k=0
    print("")
        
    
