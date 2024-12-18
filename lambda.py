add = lambda a,b:a+b

print(add(3,5))
print()

a,b=map(int,input().split())
print(add(a,b))
print()

a,b=input().split()
a=int(a)
b=int(b)
print(add(a,b))
