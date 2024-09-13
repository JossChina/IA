base = 10

spaces = 0
asterist = (base*2)-1
for lines in range(base):
    while spaces <=(base-1):
        print ('%s%s%s' %((' '*spaces),('*'*asterist),(' '*spaces)))
        spaces +=1
        asterist -=2

spaces = base-1
asterist = 1
for lines in range(base):
    while spaces >=0:
        print ('%s%s%s' %((' '*spaces),('*'*asterist),(' '*spaces)))
        spaces -=1
        asterist +=2
