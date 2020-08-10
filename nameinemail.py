string = str(input())

username=''
company = ''
for i in range(len(string)):
    if(string[i] == '@'):
        username = string[:i]
        company = string[i+1:]
print(username,company)