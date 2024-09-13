cad = "hoy es jueves"

for i in cad:
    print(i,end ='')  
print()  
x=0
while x<len(cad):
    print(cad[x],end=' ')
    x+=1
print()

cad[1]
print(cad[1:7])
print(cad[:10])
print(cad[5:3])
print(cad[::2])
