f=open('mat_dv.txt','r')
mb={}
maxa=int()
maxg=int()
for i in f:
    l=list(i.split())
    if l[2] not in mb:
        mb[l[2]]=int(l[3])+int(l[4])
    elif int(l[3])+int(l[4])>mb[l[2]]:
        mb[l[2]]=int(l[3])+int(l[4])
    if maxa<int(l[3]):
        maxa=int(l[3])
    if maxg<int(l[4]):
        maxg=int(l[4])
f.seek(0,0)
for i in f:
    l=list(i.split())
    if int(l[3])+int(l[4])==mb[l[2]]:
        print('Победитель двоебория в',l[2],'классе',l[0],l[1],int(l[3])+int(l[4]),sep=' ')
    if int(l[3])==maxa:
        print('Победитель по алгебре ',l[0],l[1],l[2],'класс',sep=' ')
    if int(l[4])==maxg:
        print('Победитель по геометрии ',l[0],l[1],l[2],'класс',sep=' ')







