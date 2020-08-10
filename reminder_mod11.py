def remainder(st) : 
    ln = len(st) 
      
    rem = 0
      
    for i in range(0, ln) : 
        num = rem * 10 + (int)(st[i]) 
        rem = num % 11
          
    return rem 
      
      
# Driver code 
st = "452"
print(remainder(st)) 