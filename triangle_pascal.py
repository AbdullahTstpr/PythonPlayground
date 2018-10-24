

L = [0,1,1,0]
intermediaire = []
for i in range(10):
    intermediaire.append(0)
    for a in range(0,len(L)-1):
        intermediaire.append(L[a]+L[a+1])
        #print(intermediaire)
    intermediaire.append(0)
    print(L)
    L = []
    L.extend(intermediaire)
    intermediaire = []



