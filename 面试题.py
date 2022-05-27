def f1(a):
    ar1 = []
    num = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    b = []
    for i in range(len(a)):
        b.append(num[int(a[i])])
    if len(b) == 1:
        ar1.append(b[0])
    else:
        ar3 = []
        b1 = b[0]
        for i in range(len(b1)):
            ar1.append(b1[i])
        for i in range(1, len(b)):
            ar2 = b[i]
            for j in range(len(ar1)):
                for k in range(len(ar2)):
                    ar3.append(ar1[j] + ar2[k])
            ar1 = ar3
            ar3 = []
    return ar1

def f2(ar):
    a=ar[0]
    if len(a)==1:
        a=a[0]
    c=[]
    for k in range(1,len(ar)):
        b=ar[k]
        if len(b)==1:
            b=b[0]
        for i in range(len(a)):
            for j in range(len(b)):
                c.append(a[i]+b[j])
        a=c
        c=[]
    for i in a:
        print(i,end=' ')

c = input('请输入内容([*,*]):')
i = False
for i in range(len(c)):
    if (c[i] == ',' and i == 1) or (c[i] == ',' and i == len(c) - 2):
        i = True
        break
if c[0] != '[' or c[len(c) - 1] != ']' or i == True:
    print('输入格式不对!')
else:
    b = []
    c2 = ''
    d=[]
    for i in range(len(c)):
        if c[i] != '[' and c[i] != ']' and c[i] != ',':
            c2 += c[i]
        if c[i] == ',' or c[i] == ']':
            b.append(c2)
            c2 = ''
    for i in range(len(b)):
        d.append(f1(b[i]))
    f2(d)