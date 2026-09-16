# s="programming"
# count=0
# for ch in s:
#     if ch in 'aeiou':
#         count+=1
# print(count)

# s="programming"
# count=0
# for ch in s:
#     if ch not in 'aeiou':
#         count+=1
# print(count)

# s="PyThOn"
# uppercase=0
# lowercase=0
# for i in s:
#     if i==i.upper():
#         uppercase+=1
#     elif i==i.lower():
#         lowercase+=1
# print("Uppercase:",uppercase)
# print("Lowercase:",lowercase)

# s = "programming"
# count=0
# for i in s:
#     if i=='g':
#         count+=1
# print(count)

# s="banana"
# freq={}
# for i in s:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)

# a="aabbcde"
# freq={}
# for i in a:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# for i in freq:
#     if freq[i]==1:
#         print(i)
#         break

# s=input("Enter a string: ")
# rev=s[::-1]
# if s==rev:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# s="python"
# r=""
# for i in range(len(s)-1,-1,-1):
#     r+=s[i]
# print(r)

# s="I love Python programming"
# count=1
# for i in s:
#     if i==" ":
#         count+=1
# print(count)

# s="I love python"
# r=""
# for i in s:
#     if i==" ":
#         continue
#     else:
#         r+=i
# print(r)

# s="programming is awesome"
# freq={}
# for i in s:
#     if i in 'aeiou':
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
# print(freq)

# s="programming"
# r=""
# for i in s:
#     if i not in r:
#         r+=i
# print(r)  

# s="programming"
# freq={}
# for i in s:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# count =0
# for i in freq:
#     if freq[i]>1:
#         count+=1
# print(count)

# s="programming"
# r=""
# for i in s:
#     if i not in r:
#         r+=i
#     elif i in r:
#         print(i)
#         break

# s1=input("Enter a string: ")
# s2=input("Enter a string: ")
# freq1={}
# freq2={}
# for i in s1:
#     if i in freq1:
#          freq1[i]+=1
#     else:
#          freq1[i]=1
# for j in s2:
#      if j in freq2:
#               freq2[j]+=1
#      else:
#               freq2[j]=1
# if freq1==freq2:
#       print("Anagram")
# else:
#       print("not")

# text = "programming"
# for i in text:
#     print(i)

# text = "programming"
# print(text[0])
# print(text[-1])
# print(text[4])

# text = "programming"
# print(text[:4])
# print(text[3:7])
# print(text[-3:])

# text = "programming"
# print(len(text))
# print(len(text)-1)

# text = "python"
# for i in range(len(text)):
#     print(i,text[i])

# first = "Deekshitha"
# last = "Nallamothu"
# print(first+" "+last)

# word = "Python"
# print(word*3)

# text = "programming"
# print("g" in text)
# print('z' in text)

# a = "python"
# b = "python"
# c = "Python"
# print(a==b)
# print(a==c)

# Input="programming"
# count=0
# for i in Input:
#     if i in 'aeiouAEIOU':
#         count+=1
# print(count)

# input='banana'
# count=0
# for i in input:
#     if i =='a':
#         count+=1
# print(count)

# text='banana'
# freq={}
# for i in text:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)

# text="banana"
# a=0
# for i in range(len(text)):
#     if text[i]=='a':
#         a=i
# print(a)

# text = "hello"
# vowels=0
# consonants=0
# for i in text:
#     if i in 'aeiouAEIOU':
#         vowels+=1
#     else:
#         consonants+=1
# print("Vowels:",vowels)
# print("Consonants:",consonants)

# text = "python"
# a=""
# for i in range(len(text)-1,-1,-1):
#     a=a+text[i]
# print(a)

# text = "madam"
# rev=text[::-1]
# if text==rev:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# text = "level"
# a=""
# for i in range(len(text)-1,-1,-1):
#     a=a+text[i]
# if text==a:
#     print("palindrome")
# else:
#     print("not")
    
# text = "hello world python"
# a=''
# for i in text:
#     if i==" ":
#         continue
#     else:
#         a=a+i
# print(a)

# text = "python12345"
# count=0
# for i in text:
#     if i in "1234567890":
#         count+=1
# print(count)

# text = "Python123@#"
# count=0
# for i in text:
#     if i.isalpha():
#         count+=1
# print(count)

# text = "PyThOn"
# uc=0
# lc=0
# for i in text:
#     if i.isupper():
#         uc+=1
#     else:
#         lc+=1
# print(uc)
# print(lc)

# text = "programming"
# a=""
# for i in text:
#     if i not in a:
#         a=a+i
# print(a)

# text = "aabbcdd"
# freq={}
# for i in text:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# for j in freq:
#     if freq[j]==1:
#         print(j)
#         break

# text1 = "listen"
# text2 = "silent"
# freq1={}
# freq2={}
# for i in text1:
#     if i in freq1:
#         freq1[i]+=1
#     else:
#         freq1[i]=1
# for j in text2:
#     if j in freq2:
#         freq2[j]+=1
#     else:
#         freq2[j]=1
# print(freq1)
# print(freq2)
# if freq1==freq2:
#     print("Anagram")
# else:
#     print("not")

# text = "mississippi"
# freq={}
# for i in text:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# max=0
# max_char=""
# for i in freq:
#     if freq[i]>max:
#         max=freq[i]
#         max_char=i
# print(max_char)

# text = "banana"
# a=""
# for i in text:
#     if i !='a':
#         a=a+i
# print(a)

# text = "aabbcde"
# frq={}
# for i in text:
#     if i in frq:
#         frq[i]+=1
#     else:
#         frq[i]=1
# for i in frq:
#     if frq[i]==1:
#         print(i)
#         break

# text = "programming"
# a=""
# for i in text:
#     if i not in a:
#         a=a+i
# print(a)

# text = "madam"
# rev=""
# for i in range(len(text)-1,-1,-1):
#     rev=text[i]+rev
# if text==rev:
#     print("Palindrome")
# else:
#     print("not")

# text = "programming"
# vowels=0
# consonants=0
# for i in text:
#     if i in 'aeiouAEIOU':
#         vowels+=1
#     else:
#         consonants+=1
# print(vowels)
# print(consonants)

# text = "mississippi"
# target = "s"
# count=0
# for i in text:
#     if i ==target:
#         count+=1
# print(count)

# text1 = "listen"
# text2 = "silent"
# freq1={}
# freq2={}
# for i in text1:
#     if i in freq1:
#         freq1[i]+=1
#     else:
#         freq1[i]=1
# for j in text2:
#     if j in freq2:
#         freq2[j]+=1
#     else:
#         freq2[j]=1
# if freq1==freq2:
#     print("Anagram")

# text = "programming"
# a=""
# for i in text:
#     if i in a:
#         print(i)
#         break
#     else:
#         a=a+i

# text = "I love Python"
# a=text.split()[::-1]
# b=" ".join(a)
# print(b)
# text = "I love programming"

# words = text.split()

# longest = ""

# for i in words:
#     if len(i) > len(longest):
#         longest = i

# print(longest)

# text1 = "abc"
# text2 = "ahbgdc"
# for i in text1:
#     print(i in text2)

# text = "aaabbc"
# freq={}
# for i in text:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# for i in freq:
#     print(f"{i}{freq[i]}")

# text = "A man, a plan, a canal: Panama"
# b=text.lower()
# a=""
# for i in b:
#     if i not in "' ,:'":
#         a=a+i

# rev=a[::-1]
# if a==rev:
#     print(True)
# else:
#     print(False)

# ransomNote = "aa"
# magazine = "aab"
# if ransomNote in magazine:
#     print(True)
# else:
#     print(False)

# text = "hello world"
# freq={}
# for i in text:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# for i in freq:
#     if freq[i]==1:
#         print(i)
#         break


# text = "programming"
# freq={}
# for i in text:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# for i in freq:
#     if freq[i]>1:
#         print(i)

# text = "abbaca"

# k = text[0]

# for i in range(1, len(text)):
#     if text[i] != text[i-1]:
#         k = k + text[i]

# print(k)

text = "aabbccdde"
freq={}
for i in text:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for i in freq:
    if freq[i]==2:
        print(i)
        break