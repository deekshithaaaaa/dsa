# Python DSA Practice

# 1. Sum of array elements
arr = [10, 20, 30, 40, 50]
total = 0
for i in arr:
    total += i
print(total)


# 2. Find largest element
arr = [10, 25, 8, 17, 30, 5, 12]
large = arr[0]
for i in arr:
    if i > large:
        large = i
print(large)


# 3. Find smallest element
arr = [10, 25, 8, 17, 30, 5, 12]
small = arr[0]
for i in arr:
    if i < small:
        small = i
print(small)


# 4. Find second smallest element
arr = [10, 25, 8, 17, 30, 5, 12]
small = arr[0]
second = arr[1]

if second < small:
    small, second = second, small

for i in range(2, len(arr)):
    if arr[i] < small:
        second = small
        small = arr[i]
    elif arr[i] < second:
        second = arr[i]

print(second)


# 5. Reverse array
arr = [10, 20, 30, 40, 50]
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end=" ")


# 6. Count even numbers
arr = [10, 25, 8, 17, 30, 5, 12]
count = 0
for i in arr:
    if i % 2 == 0:
        count += 1
print(count)


# 7. Count odd numbers
arr = [10, 25, 8, 17, 30, 5, 12]
count = 0
for i in arr:
    if i % 2 != 0:
        count += 1
print(count)


# 8. Find largest odd number index
arr = [10, 25, 8, 17, 30, 5, 12]
large = arr[0]
large_i = 0

for i in range(len(arr)):
    if arr[i] > large and arr[i] % 2 != 0:
        large = arr[i]
        large_i = i

print(large_i)


# 9. Count 2 in array
arr = [5, 2, 8, 2, 9, 5, 2]
count = 0

for i in arr:
    if i == 2:
        count += 1

print(count)


# 10. Count 5 in array
arr = [5, 2, 8, 2, 9, 5, 2]
count = 0

for i in arr:
    if i == 5:
        count += 1

print(count)


# 11. Count different numbers
arr = [5, 2, 8, 2, 9, 5, 2]
count = 0
l = []

for i in arr:
    if i not in l:
        l.append(i)
        count += 1

print(count)


# 12. Print different numbers
arr = [5, 2, 8, 2, 9, 5, 2]
l = []

for i in arr:
    if i not in l:
        l.append(i)

print(l)


# 13. Star pattern
rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# 14. Continuous number pattern
num = 0

for i in range(1, 6):
    for j in range(1, i + 1):
        print(num + j, end=" ")
    num += i
    print()


# 15. Number pattern
num = 0

for i in range(1, 6):
    for j in range(1, i + 1):
        print(num + j, end=" ")
    print()


# 16. Character pattern
c = chr(65)

for i in range(1, 5):
    for j in range(5 - i):
        c += 1
        print(c, end="")
    print()