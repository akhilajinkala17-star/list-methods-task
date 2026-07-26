#1.Remove duplicate elements.
n=[10,20,30,20,10]
result=[]
for i in n:
    if i not in result:
        result.append(i)
print(result)

#2.Count the frequency of each element.
n=['sai','ravi','chandu']
d={}
for x in n:
    if x not in d:
        d[x]=1
    else:
        d[x]=d[x]+1
print(d)

#3.Find the most frequent element.
n=['sai','chandu','bala','chandu','vinu','chandu']
max_element=''
max_count=0
for x in n:
    count=n.count(x)
    if count>max_count:
        max_count=count
        max_element=x
print("most frequent element:",max_element)
print("count:",max_count)

#4.Find the least frequent element.
n=['sai','chandu','bala','chandu','vinu','chandu']
min_element=''
min_count=len(n)
for x in n:
    count=n.count(x)
    if count<min_count:
        min_count=count
        min_element=x
print("least frequent element:", min_element)
print("count:", min_count)

#5.Check whether a given element exists.
n=[10,20,30]
element=40
if element in n:
    print("exists")
else:
    print("not exists")

#6.Find the index of an element without using index().
n=['sai','banu','chandu','ravi']
element='chandu'
for i in range(len(n)):
    if n[i]==element:
        print("Index:",i)
        break
if not element in n:
    print("Element not found")

#7.Merge two lists.
a=[10,20]
b=[30,40]
a.extend(b)
print(a)

#8.Find common elements between two lists.
n=[10,20,30]
m=[20,10,40]
result=[]
for i in n:
    if i in m:
        result.append(i)
print(result)

#9.Find elements present in the first list but not in the second.
n=[10,20,30]
m=[40,50,20]
result=[]
for i in n:
    if i not in m:
        result.append(i)
print(result)

#10.Rotate a list left by one position.
n=[10,20,30]
n=n[1:]+n[:1]
print(n)

#11.Rotate a list right by one position.
n=[1,2,3,4,5]
n=n[-1:]+n[:-1]
print(n)

#12.Rotate a list by k positions. 
n=[1,2,3,4,5]
k=2
n=n[-k:]+n[:-k]
print(n)

#13.Sort a list without using sort().
n=[5,4,6,2,3,1]
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]>n[j]:
            n[i],n[j]=n[j],n[i]
print(n)

#14.Check whether a list is sorted.
n=[1,2,3,4,5]
is_sorted=True
for i in range(len(n)-1):
    if n[i]>n[i+1]:
        is_sorted=False
        break
if is_sorted:
    print("sorted")
else:
    print("not sorted")
    
#15.Split a list into two equal halves.
n=[1,2,3,4,5,6]
list1=[]
list2=[]
for i in range(len(n)):
    if i<len(n)//2:
        list1.append(n[i])
    else:
        list2.append(n[i])
print(list1)
print(list2)
     

