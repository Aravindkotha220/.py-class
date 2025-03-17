

my_list = [1, 2, 4, 6, "True", False, 24]
search_ele = 23

def check_if_ele_present(input_list, ele):
    return ele in input_list 

def search_ele_index(input_list, ele):
    for i in range(len(input_list)):
        if ele == input_list[i]:
            return i 
    return -1

print(search_ele_index(my_list, 24)) 
print(search_ele_index(my_list, 23)) 

        
# finding duplicate in list

# list=[1,1,1,4,3,6,5,6,6,2,2,7,8,]
# visited_list=[]
# for i in list:
#     if i in visited_list:
#         print(i,"is duplicate")
#     else:
#             visited_list.append(i)

list=[1,1,1,4,3,6,5,6,6,2,2,7,8,]
visited_list=[]
output_set=set()
for i in list:
    if i in visited_list:
        # print(i,"is duplicate")
        output_set.add(i)
    else:
            visited_list.append(i)
    print(output_set)
    
    
    # 

def check_dup_digit(n):
    vis_list = []  
    temp = n     

    while temp > 0:
        digit = temp % 10 
        if digit in vis_list:
            return True 
        else:
            vis_list.append(digit) 
        temp = temp // 10 
    return False 
num = int(input("Enter a number: "))
print(check_dup_digit(num))
    
      
    #   
                
def check_dup_digit(n):
    str_n = str(n)
    return len(set(str_n)) != len(str_n)

list1 = [1232, 334, 72, 81, 223]
output_list1 = []

for i in list1:
    res = check_dup_digit(i)
    output_list1.append(res)

print(output_list1)