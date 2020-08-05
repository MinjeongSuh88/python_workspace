m=[]
m.append([100,200])
m.append([300,400,500,600,700])
m.append([900,1000,1100])
print(m)
print(m[1][3])

print(m[0][0])
print(m[0][1])


for i in range(2):
    print(m[0][i],end=',')
print()


for j in range(5):
    print(m[1][j],end=',')
print()

for k in range(3):
    print(m[2][k],end=',')
print()

for i in range(3): # 2차문 배열
    for j in range(len(m[i])):
        print(m[i][j])
print(len(m[1]))
print(len(m[2]))
            
n=[]
n.append([100,50,30,20])
n.append([200,100,])
n.append([900,1000,20,20,30,40,50])
n.append([50,70,90,])
for j in range(4):
    for j in range(len(n[i])):
        print(n[i][j])

