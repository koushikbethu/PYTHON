numbers=[10,2,30,4,32,56]

total_sum=sum(numbers)
count=len(numbers)

average=(total_sum/count)
print(f"the average of the list is :{average:.2f}" )

average=round((total_sum/count))
print(f"the rounded to the nearest integer,  average of the lsit is : {(total_sum/count)}")
