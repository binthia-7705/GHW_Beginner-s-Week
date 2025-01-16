#Bubble sort
a=int(input("Enter noof elements in list: " ))
l=[]
for i in range(a):
    x=int(input("Enter the element: "))
    l.append(x)

print(f"Orginal list {l}")
for i in range(a):
    for j in range (0,a-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(f"List after sorting {l}")
