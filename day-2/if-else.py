
# num=int(input("enter the number:"))

# if num==0:
#     print('nor positive')
# elif num == 1:
#     print('one')
# elif num>0:
#     print('postive num')    
# elif num==-2:
#     print('negative num')        
# else:
#     print('negitive')    


current_bill_units=int(input('enter the units '))
if current_bill_units<=100:
    
    if current_bill_units<=50:
      print( "rupees:",0*current_bill_units )
    else:
        print("rupees:",50*current_bill_units )  
else:
    if current_bill_units<=200:
        print( "rupees:",100*current_bill_units)
    else:
        print("rupees:",150*current_bill_units)        
