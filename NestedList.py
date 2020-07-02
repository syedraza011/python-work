if __name__ == '__main__':
    N=int(input())
    ml=[]
    for i in range(N):
        el=[]
        el.append((input()))
        no=float(input())
        
        el.append(no)
        ml.append(el)

    nl=[]
    for i in range (N):
        nl.append(ml[i][1])
    nnl=sorted(nl)

    mino=nnl[0]
    for i in range(N):
        if nnl[i]>mino:
            op=nnl[i]
            break
            
    fl=[]
    for i in range(N):
        for j in range(2):
            if ml[i][1]==op:
                fl.append(ml[i][0])
            break
    fl.sort()
    for i in fl:
        print(i)