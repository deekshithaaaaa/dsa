class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
head=n1
n1.next=n2
n2.next=n3
current=head
count=0
while current:
    
    count+=1
    current = current.next
print(count)

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n1.next=n2
n2.next=n3
head=n1
current = head

while current:
    if current.data == 50:
        print(True)
        break
    current = current.next
else:
    print(False)

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(10)
n2=Node(50)
n3=Node(30)
n4=Node(20)
n1.next=n2
n2.next=n3
n3.next=n4
head=n1
current=head
max=current.data
while current:
    if current.data>max:
        max=current.data
    current=current.next
print(max)

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(40)
n2=Node(10)
n3=Node(30)
n4=Node(20)
n1.next=n2
n2.next=n3
n3.next=n4
head=n1
current=head
min=float('inf')
while current:
    if current.data<min:
        min=current.data
    current=current.next
print(min)

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(10)
n4=Node(30)
n5=Node(10)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
head=n1
current=head
count=0
while current:
    if current.data==10:
        count+=1
    current=current.next
print(count)

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(10)
n4=Node(30)
n5=Node(10)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
head=n1
current=head
count=0
while current:
    count+=1
    current=current.next
print(count)

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n1.next=n2
n2.next=n3
n3.next=n4
head=n1
current=head
while current:
    if current.data==30:
        print("Found")
        break
    current=current.next
else:
    print("Not Found")

