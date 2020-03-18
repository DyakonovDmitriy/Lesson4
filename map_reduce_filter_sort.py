# map

def miles_to_km(miles):
    return miles*1.6

mail_dist=[1.0,1.6,2.3]

# km_dist=map(miles_to_km,mail_dist)
# print(km_dist)


km_dist=list(map(lambda x: x*1.6, mail_dist))
print(km_dist)

list1=[1,2,3]
list2=[4,5,6]
list3=list(map(lambda x,y:x+y,list1,list2))
print(list3)

# reduce

from functools import reduce

list_temp=[5,345,65,76]
max=reduce(lambda x,y: x if x>y else y,list_temp)
print(max)

#filter

list_proba=[134,234,324,5,56,67,123]
list_50=list(filter(lambda x: x>50,list_proba))
print(list_50)

#sort

list_temp_sort=(list_temp.reverse())
print(list_temp_sort)

list_names=['Kate','Dima','Ivan','Mike']
sort_name=sorted(list_names, key= lambda x: x[1])
print(sort_name)