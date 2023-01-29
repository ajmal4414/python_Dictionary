#2. python script to concatonate two dictionaries to create a new one

dict1={'john':20,'sajin':30}
dict2={'tom':40,'akhil':50}


dict3={}

for d in (dict1,dict2,):  #d1,d2
    dict3.update(d)           #1updating dict
print(dict3)