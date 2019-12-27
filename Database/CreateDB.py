import pymysql

conn = pymysql.connect('localhost','root','MySQL0330','adult')

print "Opened database successfully"
c = conn.cursor()

c.execute('''create table adultinfo(
            id int primary key not null,
            age int,
            workclass varchar(30),
            fnlwgt varchar(20),
            education varchar(20),
            education_num int,
            marital_status varchar(30),
            occupation varchar(20),
            relationship varchar(20),
            race varchar(20),
            sex varchar(10) check(sex='male' or sex='female'),
            capital_gain int,
            capital_loss int,
            hours_per_week int,
            native_country varchar(30),
            salary varchar(10) check(salary='<=50k' or salary='>50k')
            );''')
print "Table creates success"
conn.commit()
conn.close()