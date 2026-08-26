arr = [2, 4, 1, 6, 3]
prefix=[]
for i in range(len(arr)):
    if i==0:
        prefix.append(arr[i])
    else:
        prefix.append(prefix[i-1]+arr[i])
print(prefix)

arr = [5, 3, 7, 2, 4]
prefix = [5, 8, 15, 17, 21]
l=2
r=4
res=prefix[r]-prefix[l-1]
print(res)

arr = [4, 2, 7, 3, 5, 1]
pre=[]
for i in range(len(arr)):
    if i==0:
        pre.append(arr[i])
    else:
        pre.append(pre[i-1]+arr[i])
l=1
h=4
res=pre[h]-pre[l-1]
print(res)

arr = [2, 4, 1, 6, 3, 5]
pre=[]
for i in range(len(arr)):
    if i==0:
        pre.append(arr[i])
    else:
        pre.append(pre[i-1]+arr[i])
l=int(input())
r=int(input())
if l==0:
    print(pre[r])
else:
    print(pre[r]-pre[l-1])

