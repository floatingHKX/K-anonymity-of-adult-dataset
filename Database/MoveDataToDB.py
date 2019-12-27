#coding=utf-8
import pymysql

#连接数据库
conn = pymysql.connect('localhost','root','MySQL0330','adult')
print "Opened database successfully"
c = conn.cursor()

file = open("../adult.data","r")
line = file.readline()
cord = 0
sqlstr = '''insert into adultinfo (id, age, workclass, fnlwgt, 
                                education, education_num, marital_status, 
                                occupation, relationship, race, sex, capital_gain,
                                capital_loss, hours_per_week,
                                native_country, salary)
            values (%s, %s, %s, %s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s)'''
while line:
    #print line
    line = line[:-1]
    if line == "":
        break
    content = line.split(", ")
    c.execute(sqlstr,(cord,content[0],content[1],content[2],content[3],content[4],content[5],content[6],content[7],
                      content[8],content[9],content[10],content[11],content[12],content[13],content[14]))
    print content
    line = file.readline()
    cord += 1

file.close()
print 'over'
conn.commit()
conn.close()

