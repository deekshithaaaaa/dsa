arr = [4, 1, 6, 3, 8, 2]
target = 10
seen=set()
for i in arr:
    wanted=target-i
    if wanted in seen:
        print(i,wanted)
    seen.add(i)

arr = [4, 2, 7, 2, 5, 4, 8]
seen=set()
for i in arr:
    if i in seen:
        print("Found duPLICATE-",i)
        break
    seen.add(i)

arr = [4, 2, 7, 2, 5, 4, 8]
seen=set()
for i in arr:
    if i in seen:
        print(i)
    seen.add(i)
arr = [1, 3, 5, 3, 7, 1, 9, 5]
seen = set()
duplicates = set()

for i in arr:

    if i in seen:
        if i not in duplicates:
            print(i)
            duplicates.add(i)

    seen.add(i)

arr = [2, 4, 2, 7, 4, 2, 8, 7]
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

arr = [2, 4, 2, 7, 4, 2, 8, 7]
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for i in arr:
    if freq[i]==1:
        print(i)
        break

s = "swiss"
freq={}
for i in s:
    
     if i in freq:
        freq[i]+=1
     else:
        freq[i]=1
for i in s:
   if freq[i]==1:
      print(i)
      break
