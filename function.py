def sumupto(n):
    sum=0
    for i in range(n+1):
        sum +=i
    return sum

number=int(input("Enter the number :"))
result=sumupto(number)
print(f"the sum upto {number} is {result}.")

