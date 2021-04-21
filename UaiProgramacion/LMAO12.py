n = str(input("numero: "))
g=list(n)
l = []
nn = int(n)
m = len(n)
p=0
while p < m:

    for i in range(0,(m-p)):
        num = ""
        c = 0
        while c <= i:
            num = num + g[c]
            c = c+1
        l.append(int(num))
    del g[0]
    p+=1
t=0
for a in l:
    s=0
    if a != 1:
        for z in range(2, a+1):
            if a % z == 0:
                s = s + 1
    else:
        s=s+2
    if s < 2:
        t+=1
print(t)

