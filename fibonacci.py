################
#Fibonnaci
################
L = []
a = 1
b = 1
for i in range(100):
    c=a+b
    a=b
    b=c

    somme = 0
    
    for chars in str(c):
        somme += int(chars)
        
    print("Fibonacci no "+str(i+3)+" : "+str(c)+" sum:"+str(somme))
    
