#dictionary operations

#copyfunction
dict1={'bank':'federal bank', 'phone no':12122122, 'branch':'kochi'}
print(dict1)
a=dict1.copy()
print(a)

#clearmethod
dict2={'bank':'federal bank', 'phone no':12122122, 'branch':'kochi'}
print(dict2)
z=dict2.clear()
print(dict2)

# dict.item method
dict3={'bank':'federal bank', 'phone no':12122122, 'branch':'kochi'}
print(dict3)
print(dict3.items())

#dict.key method
dict4={'bank':'federal bank', 'phone no':12122122, 'branch':'kochi'}
print(dict4)
print(dict4.keys())

#dict.value method
dict5={'bank':'federal bank', 'phone no':12122122, 'branch':'kochi'}
print(dict5)
print(dict5.values())

#dict.update method
dict6={'bank':'federal bank', 'phone no':12122122, 'branch':'kochi'}
print(dict6)
dict7={'other branches':'palakkad'}
print(dict7)
dict6.update(dict7)

#len method
dict9={'bank':'federal bank', 'phone no':12122122, 'branch':'kochi'}
print(dict9)
print(len(dict9))

# popitem method
dict10={'bank':'federal bank', 'phone no':12122122, 'branch':'kochi'}
print(dict10)
a=dict10.popitem()
print(a)

#pop method
dict11={'bank':'federal bank', 'phone no':12122122, 'branch':'kochi'}
print(dict11)
print(dict11.pop('phoneno',12122122))

#set default
dict12={'bank':'federal bank', 'phone no':12122122, 'branch':'kochi'}
print(dict12)
print(dict12.setdefault('mobileno','232323'))
print(dict12)

#get method
dict13={'bank':'federal bank', 'phone no':12122122, 'branch':'kochi'}
print(dict13)
print(dict13.get('bank'))

# #del method
# dict15={'bank':'federal bank', 'phone no':12122122, 'branch':'kochi'}
# print(dict15)
# print(dict15.del('bank'))
