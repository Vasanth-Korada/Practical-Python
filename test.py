no_of_commands = int(input())
list1 = []
for i in range(no_of_commands):
    name,*list = input().split()
    if(name == "insert"):
        list1.insert(int(list[0]),int(list[1]))
print(list1)            
