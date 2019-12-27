# encoding: utf-8

AttrStatistics = []
AttrName = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation',
            'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'salary']


file = open("adult.data","r")
line = file.readline()

for i in range(0, len(AttrName)):
    dict = {}
    AttrStatistics.append(dict)

# 创建4个集合，用来保存QID中的值
education_set=set()
education_num_set=set()
race_set=set()
native_country_set=set()
# native_country_set=set()

while line:
    #print line
    line = line[:-1]
    if line == "":
        break
    content = line.split(", ")
    #print content
    for i in range(0, len(content)):
        val = content[i]
        cord = AttrStatistics[i].get(val)
        if cord == None:
            AttrStatistics[i][val] = 1
        else:
            AttrStatistics[i][val] = cord + 1
    line = file.readline()

    # 将属性值存入集合
    education_set.add(content[3])
    education_num_set.add(content[4])
    race_set.add(content[8])
    native_country_set.add(content[13])
    # native_country_set.add(content[13])

for i in range(0, len(AttrStatistics)):
    dict = AttrStatistics[i]
    print (AttrName[i] + "\t" + str(len(dict.items())))
# 
education_list=list(education_set)
education_num_list=list(education_num_set)
race_list=list=(race_set)
native_country_list=list=(native_country_set)
# native_country_list=list(native_country_set)

print('======================================')
print(education_list)
print('======================================')
print(education_num_list)
print('======================================')
print(race_list)
print('======================================')
print(native_country_list)
# print(native_country_list)

#print AttrStatistics