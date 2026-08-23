s="programming"
count=0
for ch in s:
    if ch in 'aeiou':
        count+=1
print(count)

s="programming"
count=0
for ch in s:
    if ch not in 'aeiou':
        count+=1
print(count)

s="PyThOn"
uppercase=0
lowercase=0
for i in s:
    if i==i.upper():
        uppercase+=1
    elif i==i.lower():
        lowercase+=1
print("Uppercase:",uppercase)
print("Lowercase:",lowercase)

s = "programming"
count=0
for i in s:
    if i=='g':
        count+=1
print(count)

s="banana"
freq={}
for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

a="aabbcde"
freq={}
for i in a:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for i in freq:
    if freq[i]==1:
        print(i)
        break

s=input("Enter a string: ")
rev=s[::-1]
if s==rev:
    print("Palindrome")
else:
    print("Not a Palindrome")

s="python"
r=""
for i in range(len(s)-1,-1,-1):
    r+=s[i]
print(r)

s="I love Python programming"
count=1
for i in s:
    if i==" ":
        count+=1
print(count)

s="I love python"
r=""
for i in s:
    if i==" ":
        continue
    else:
        r+=i
print(r)

s="programming is awesome"
freq={}
for i in s:
    if i in 'aeiou':
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
print(freq)

s="programming"
r=""
for i in s:
    if i not in r:
        r+=i
print(r)  

s="programming"
freq={}
for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
count =0
for i in freq:
    if freq[i]>1:
        count+=1
print(count)

s="programming"
r=""
for i in s:
    if i not in r:
        r+=i
    elif i in r:
        print(i)
        break

s1=input("Enter a string: ")
s2=input("Enter a string: ")
freq1={}
freq2={}
for i in s1:
    if i in freq1:
         freq1[i]+=1
    else:
         freq1[i]=1
for j in s2:
     if j in freq2:
              freq2[j]+=1
     else:
              freq2[j]=1
if freq1==freq2:
      print("Anagram")
else:
      print("not")

