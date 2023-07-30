
dict1 = {'StdNo':'010','StuName': 'Ritish Bhatoye', 'StuAge': 19, 'StuCity': 'Jalandhar'}
print("\n Dictionary is :",dict1)
print("\n Student Name is :",dict1['StuName'])
print("\n Student City is :",dict1['StuCity'])
print("\n All Keys in Dictionary ")
for x in dict1:
    print(x)
print("\n All Values in Dictionary ")
for x in dict1:
    print(dict1[x])
dict1["Phno"]=7087963595
print("\n Uadated Dictionary is :",dict1)
dict1["StuName"]="Rahul"
print("\n Uadated Dictionary is :",dict1)
dict1.pop("StuAge");
print("\n Uadated Dictionary is :",dict1)
print("Length of Dictionary is :",len(dict1))
dict2=dict1.copy()
print("\n New Dictionary is :",dict2)
dict1.clear()
print("\n Uadated Dictionary is :",dict1)
