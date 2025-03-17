list=[1,6,97,-76,54,7]
sum=0
for i in range(0,len(list),2):
      if list[i]%2==0:
            sum+=list[i]
    
print(sum)




# for finding even numbers

for i in range(0, len(list1), 2):
   if (list1[i] % 2 == 0):
        sum += list1[i]
        
        
        
        # for finding max value 
        list = [2,3,4,5,6,7]
max = list[0]
for i in list :
    if i > max:
        max = i
print(max)


# for finding min value
list=[1,6,97,-76,54,7]
if len(list)>0:
    min=list[0]
    max=list[0]
    for i in list:
        if i>max:
            max=i
        if i<min:
            min=i
    print(max)
    print(min)
else:
    print("Empty list")