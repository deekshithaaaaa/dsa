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


arr = [10, 20, 30, 40, 50]
for x in arr:
    print(x)

arr = [10, 20, 30, 40, 50]
for i in range(len(arr)):
    print(arr[i])

arr = [10, 15, 22, 33, 40, 51]
for i in arr:
    if i%2==0:
        print(i)

arr = [12, 45, 7, 89, 23, 56]
largest=0
for i in arr:
    if i>largest:
        largest=i
print(largest)

arr = [12, 45, 7, 89, 23, 56]
smallest=arr[0]
for i in arr:
    if i<smallest:
        smallest=i
print(smallest)

arr = [10, 15, 22, 33, 40, 51, 60]
count=0
for i in arr:
    if i%2==0:
        count+=1
print(f"Even count={count}")

arr = [-5, 10, -2, 7, 0, 15, -8, 20]
count=0
for i in arr:
    if i>0:
        count+=1
print(f"Positive numbers count is {count}")

arr = [10, 20, 30, 40, 50]
sum=0
for i in arr:
    sum=sum+i
print(sum)

arr = [10, 20, 30, 40, 50]
total=0
for i in arr:
    total+=i
avg=total/len(arr)
print(avg)

arr = [12, 45, 7, 89, 23, 56]
largest=arr[0]
index=0
for i in range(len(arr)):
    if arr[i]>largest:
        largest=arr[i]
        index=i
print(f"largest: {largest}")
print(f"index is: {index}")

arr = [10, 20, 10, 30, 10, 40, 20]
count=0
for i in arr:
    if i==10:
        count+=1
print(f"10 occured {count} times")

arr = [5, 8, 2, 8, 9, 8, 3]

for i in range (len(arr)):
    if arr[i]==8:
        print(i)
        break

arr = [5, 8, 2, 8, 9, 8, 3]
index=0
for i in range(len(arr)):
    if arr[i]==8:
        index=i
print(index)

arr = [3, 7, 2, 9, 5]
for i in range(len(arr)-1,-1,-1):
    print(arr[i])

arr = [-5, 10, 0, -2, 7, 0, 15, -8]
positive=0
negative=0
zero=0
for i in arr:
    if i>0:
        positive+=1
    elif i==0:
        zero+=1
    else:
        negative+=1
print("Positive:",positive)
print("Negative:",negative)
print("Zero:",zero)

arr = [10, 5, 20, 8, 20, 15]
largest=float('-inf')
second=float('-inf')
for i in arr:
    if i>largest:
        second=largest
        largest=i
    elif second<i and i<largest:
        second=i

print(second)

arr = [10, 5, 20, 8, 20, 15]
small=float('inf')
second=float('inf')
for i in arr:
    if i<small:
        second=small
        small=i
    elif i<second and i>small:
        second=i
print(second)

arr = [2, 5, 8, 12, 15]

is_sorted = True

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        is_sorted = False
        break

if is_sorted:
    print("Array is sorted")
else:
    print("Array is not sorted")

arr = [2, 5, 4, 8, 10]
is_sorted=True
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        is_sorted=False
if is_sorted:
    print("array is sorted")
else:
    print("array is not sorted")

arr = [10, 20, 30, 40, 50]

left = 0
right = len(arr) - 1

while left < right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1

print(arr)

arr = [5, 10, 15, 20, 25]
first=arr[0]
for i in range(len(arr)-1):
    arr[i]=arr[i+1]
arr[len(arr)-1]=first
print(arr)

arr = [10, 20, 30, 40, 50]
first=arr[0]
second=arr[1]
for i in range(len(arr)-1):
    arr[i]=arr[i+1]
for i in range(len(arr)-1):
    arr[i]=arr[i+1]
arr[len(arr)-1]=second
arr[len(arr)-2]=first
print(arr)
       
arr = [5, 10, 15, 20, 25]
first=arr[len(arr)-1]
for i in range(len(arr)-1,0,-1):
    arr[i]=arr[i-1]
arr[0]=first
print(arr)

arr = [10, 20, 30, 40, 50]
k = 3
for j in range(k):
    first = arr[0]
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]
    arr[-1]=first
print(arr)

arr = [5, 10, 15, 20, 25]
k = 2
for j in range(k):
    first=arr[0]
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]
    arr[-1]=first
print(arr)

arr = [5, 10, 15, 20, 25]
k = 2
for j in range(k):
    last=arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=last
print(arr)

arr = [2, 3, 2, 5, 3, 2]
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

arr = [4, 2, 4, 7, 4, 2, 9]
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq[4])

arr = [5, 2, 5, 3, 2, 5, 3]
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

arr = [2, 5, 3, 2, 7, 5, 8]
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for i in freq:
    if freq[i]>1:
        print(i)

arr = [2, 5, 3, 2, 7, 5, 8]
a=[]
for i in arr:
    if i not in a:
        a.append(i)
print(a)

arr = [1, 2, 4, 5]
missing=0
for i in range(len(arr)):
    if arr[i]!=i+1:
        missing=i+1
        break
print(missing)

arr = [2, 7, 11, 15]
target = 9
for i in range(len(arr)):
    if arr[i]+arr[i+1]==target:
        print(arr[i],arr[i+1])
        break

arr = [2, 11, 7, 15]
target = 9
for i in range (len(arr)):
    for j in range (i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print(arr[i],arr[j])
            break

arr = [3, 8, 4, 12, 6]
target = 10
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print(arr[i],arr[j])
            break

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
for i in arr2:
    arr1.append(i)
print(arr1)

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
for i in arr1:
    if i in arr2:
        print(i)

arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]
for i in arr2:
    if i not in arr1:
        arr1.append(i)
print(arr1)

arr = [1, 2, 3]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        
        print(sum(arr[i:j+1]))

arr = [1, 3, 2, 4]
a=[]
total=0
for i in range(len(arr)):
    total=arr[i]+total
    a.append(total)
print(a)

arr = [2, 4, 3, 5, 6]
a=[]
total=0
for i in range(len(arr)):
    total=arr[i]+total
    a.append(total)
left=1
right=3
sum=a[right]-a[left-1]
print(sum)

arr = [5, 2, 7, 3, 6]
a=[]
total=0
for i in range(len(arr)):
    total=arr[i]+total
    a.append(total)
left = 2
right = 4
summ=a[right]-a[left-1]
print(summ)

arr = [-2, 3, -1, 5]
cur_sum=0
max_sum=0

for i in range(len(arr)):
   cur_sum=max(arr[i],arr[i]+cur_sum)
   max_sum=max(max_sum,cur_sum)
print(max_sum)
         
arr = [-5, 2, -1, 3, -2, 4, -10]
cur_sum=0
max_sum=0
for i in range(len(arr)):
    cur_sum=max(arr[i],arr[i]+cur_sum)
    max_sum=max(max_sum,cur_sum)
print(max_sum)

arr = [2, 5, 1, 4, 3]
k = 3

window_sum = 0
for i in range(k):
    window_sum=arr[i]+window_sum
print(window_sum)


