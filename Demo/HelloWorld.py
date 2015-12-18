print('Hello World')
print(2**100)
p=(4,5)
x,y=p
print(x)
z=float(1+2.0+3)
print(z)
for x in [1,2,3]:
    print(x,end='')

res=[c*4 for c in 'SPAM']
print(res)
res=[]
for C in 'SAPM':
    res.append(C*4)

    print(res)

list(map(abs,[-1,-2,0,1,2]))
L=['spam','Spam','SPAM!']
L[1]='eggs'
print(L)

if not 1:
    print('true')
else:
    print('false')

import threenames
print(threenames.a,threenames.c)
print(dir(threenames))#返回模块内部所有属性
S='SPAM'
print(len(S))
print(S[0])
print(S[-1])#反向索引从有右边开始计算
print(S[-2])
print(S[1:3])#分片1到2
print(S[1:])
print(S[:])
#Python 不可以直接改变变量值，但可以重新创建一个相同名称的变量然后赋值



