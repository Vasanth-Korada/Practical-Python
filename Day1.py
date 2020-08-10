#Day 1


table_number = int(input("Enter table number:"))
end_number = int(input("Enter end number:"))

for i in range(1,end_number+1):
    print ("{}*{}={}".format(table_number,i,table_number*i))

