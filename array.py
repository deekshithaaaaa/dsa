arr = [4, 2, 4, 1, 2, 5, 1, 6]
arr1=[]
for i in arr:
    if i in arr1:
        continue
    else:
        arr1.append(i)
print(arr1)

s = "aabbcddeff"
r=""
for i in s:
    if i not in r:
        print(i)
        break
    else:
        r+=i

arr = [0, 1, 0, 3, 12]
arr1=[]
for i in arr:
    if i!=0:
        arr1.append(i)
for i in arr:
    if i==0:
        arr1.append(i)
print(arr1)

s1 = "listen"
s2 = "silent"
freq1={}
freq2={}
if len(s1)!=len(s2):
    print("Not")
for i in s1:
    if i in freq1:
        freq1[i]+=1
    else:
        freq1[i]=1
for i in s2:
    if i in freq2:
        freq2[i]+=1
    else:
        freq2[i]=1
if freq1==freq2:
    print("Anagram")
else:
    print("Not")

arr = [10, 5, 10, 8, 12, 12, 7]
l=float("-inf")
sl=float("-inf")
for i in arr:
    if i>l:
        sl=l
        l=i
    elif i>sl and i<l:
        sl=i
print(sl)

s = "Python is very powerful language"
t = s.split()
large = ""
for i in t:
    if len(i) > len(large):
        large = i
print(large)

arr1 = [1, 2, 2, 3, 4, 5]
arr2 = [2, 2, 4, 4, 6]
a=set(arr1)
b=set(arr2)
for i in a and b:
    if i in a and b:
        print(i)

s1 = "programming"
s2 = "ram"
r=""
for i in s1:
    if i not in s2:
        r+=i
print(r)


