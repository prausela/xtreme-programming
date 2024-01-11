
###########################################################
# BeetleBug                                               #
###########################################################
# Beetleman joined the Strangers, a team of super heroes  #
# who protect cyber world.                                #
#                                                         #
# In order to increase Beetleman's fighting power,        #
# Copperman allowed Beetleman to choose gadgets from his  #
# labs freely.                                            #
#                                                         #
# However, Beetleman has limited space in his hero bag.   #
#                                                         #
# Your task is to help Beetleman choose gadgets to        #
# increase his fighting power as much as possible.        #
#                                                         #
###########################################################

t = int(input())

for ti in range(t):
    line = input()
    line = line.split()
    
    c = int(line[0])
    n = int(line[1])
    
    G = list()
    
    for ni in range(n):
        line = input()
        line = line.split()
        
        w = int(line[0])
        f = int(line[1])
        
        G.append((w, f))
        
    max_f = 0
        
    s = list()
    s.append((n-1, 0, 0))
    
    while len(s) > 0:
        ni, w, f = s.pop()
        
        if ni < 0:
            max_f = max(max_f, f)
        elif w < c:
            s.append((ni-1, w + G[ni][0], f + G[ni][1]))
            s.append((ni-1, w, f))
            
    print(max_f)