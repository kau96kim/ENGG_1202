def applyMove(state, move):
    new=list(state)
    if move=='PUSH':
        for i in range(len(state)):
            if state[i]==0 and i!=0:
                new[i-1]=state[i]
                new[i]=state[i-1]
    elif move=='PULL':
        for i in range(len(state)):
            if state[i]==0 and i<len(state)-1:
                new[i]=state[i+1]
                new[i+1]=state[i]
    elif move=='SWAP':
        for i in range(len(state)):
            if state[i]==0 and i>1:
                new[i-2]=state[i-1]
                new[i-1]=state[i-2]
    elif move=='FLIP':
        count=1;
        for i in range(len(state)):
            if state[i]==0 and i<len(state)-1:
                for j in range(i+1, len(state)):
                    new[j]=state[len(state)-count]
                    count=count+1;
    return (tuple(new));
    
def h(state):
    a=0;
    holder=True;
    for i in range(len(state)):
        if state[i]==0:
            holder=False;
        if holder==True:
            a=a+1;
    a=a*10;
    
    b=0;
    ball=state[0];
    for i in range(len(state)-1):
        if ball<state[i+1]:
            ball=state[i+1];
        elif state[i+1]!=0:
            b=b+1;
    
    c=0;
    ball=state[len(state)-1];
    for i in range(len(state)-1):
        if ball<state[len(state)-2-i]:
            ball=state[len(state)-2-i];
        elif state[len(state)-2-i]!=0:
            c=c+1;
            
    d1=b*17
    d2=8+c*17
    if d1<d2:
        d=d1
    else:
        d=d2
    return d+a
    
def getNext(frontier):
    matrix=frontier[0]
    ans=h(frontier[0]['state'])+temp(frontier[0]['path'])
    for f in frontier:
        if ans > h(f['state'])+temp(f['path']) :
            ans = h(f['state'])
            matrix = f
    frontier.remove(matrix)
    return matrix
    
def temp (frontier):
    ans=0
    for i in frontier:
        if i=='PUSH':
            ans=ans+10
        elif i=='PULL':
            ans=ans+5
        elif i=='SWAP':
            ans=ans+17
        elif i=='FLIP':
            ans=ans+8
    return ans