base = 10

spaces = base-1
asterist = 1
for lines in range(base):
    while spaces >=1:
        print ('%s%s' %(('*'*asterist),(' '*spaces)))
        spaces -=1
        asterist +=2
    
