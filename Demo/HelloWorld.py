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
S='z'+S[1:]
print(S)
q=S.find('ps')
print(q)
S.replace('pa','XYZ')#但不会改变原来的变量

line='aaa,bbb,ccc,dd'
print(line.split(','))
print(S.upper())

print('%s,eggs,and %s'%('spam','SPAM!'))
print('{0},eggs,and {1}'.format('spam','SPAM!'))#高级格式化

L=[123,'spam',1.23]
L.append('NI')
L.pop(2)
print(L)#大多数列表的方法可以直接改变列表的值
M=['bb','aa','cc']
M.sort()
print(M)
M.reverse()#翻转
print(M)
M=[[1,2,3],[4,5,6],[1,8,9]]
print(M)
print(M[1])
#列表解析假设我们需要从矩阵中提取第二列
col2=[row[1] for row in M]
print(col2)
#print(row[1]+1 for row in M)
diag=[M[i][i] for i in [0,1,2]]
print(diag)

douebles=[c*2 for c in 'spam']
print(douebles)
G=(sum(row) for row in M)
print(next(G))
#字典
D={'food':'spam','quantity':4,'color':'pink'}
print(D['food'])
print(D['quantity']+1)
D['quantity']+=1
D['name']='Bob'
D['job']='dev'

print(D)

res={'name':{'first':'Bob','last':'Smith'},'job':['dev','mgr'],'age':45.5}

print(res)
print(res['name'])
print(res['name']['first'])
print(res['name']['last'])
print(res['job'][0])
print(res['job'].append('janitor'))
print(res)

D={'a':1,'b':2,'c':3}
print(D)
#字典的排序
Ks=list(D.keys())
print(Ks)
Ks.sort()
print(Ks)
for key in Ks:
    print(key,'=>',D[key])

for key in sorted(D):
    print(key,'=>',D[key])

for c in 'spam':
    print(c.upper())

x=4
while x>0:
    print('spam!'*x)
    x-=1

#元组相当于一个不可以改变的列表
T=(1,2,34)
print(len(T))
T+=(5,6)
print(T)
print(T.count(4))#元素4出现的次数


#文件操作--创建一个文件然后写入
f=open('data.txt','w')
f.write('Hello\n')

w=open('data.txt')
text=w.readline()
print(text)#读不出来？？？

#集合类型
X=set('spam')
Y={'h','a','m'}
print(X,Y)
print(X&Y)
print(X|Y)
print(X-Y)
print({k**2 for k in [1,2,3,4]})

#定义类
class Worker:
    def __init__(self,name,pay):#初始化了两个属性name和pay
        self.name=name
        self.pay=pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay*=(1+percent)

bob=Worker('Bob Smith',50000)
sue=Worker('Sue Jones',60000)
print(bob.lastName())
print(sue.lastName())
sue.giveRaise(.10)
print(sue.pay)



