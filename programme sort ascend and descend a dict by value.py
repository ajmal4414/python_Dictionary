#1. programme to sort (ascending and descending) a dictionary by value

import operator

dic = {1:2, 3:4, 4:3, 2:1, 0:0}
print("original dictionary:" ,dic)

sorted_dic =sorted(dic.items(),key=operator.itemgetter(1)) #key any data type
print("dictionary in ascending order by value:", sorted_dic)

sorted_dic =sorted(dic.items(),key=operator.itemgetter(1), reverse=True)
print("dictionary in descending order by value:",sorted_dic)
