#encoding:utf-8
import MySQLdb

conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='mypassword',
        charset = "utf8",
        db='university',
    )
t = conn.cursor()

# t.execute("load data infile '/home/ben/下载/MySQL-python-1.2.3/university/student.txt' into table student(ID,name,sex,age,emotion_state,dept_name)")
# t.execute("load data infile '/home/ben/下载/MySQL-python-1.2.3/university/exam.txt' into table exam(student_ID,examname,mark)")
# t.execute("load data infile '/home/ben/下载/MySQL-python-1.2.3/university/department.txt' into table department(dept_name,buildin,budget)")

with open("/home/ben/university/department.txt","r") as f:
    while True:
        line = f.readline()
        if line:
            line = line.strip('\n')
            line = line.split(' ')
            print (line)
            dept_name = line[0]
            building = line[1]
            budget = line[2]
            t.execute(
                 "insert into department(dept_name,building,budget)values(%s,%s,%s)",
                [dept_name,building,budget])
            conn.commit()
        else:
            pass



with open("/home/ben/university/exam.txt","r") as g:
    while True:
        line = g.readline()
        if line:
            line = line.strip('\n')
            line = line.split(' ')
            print (line)
            student_ID = line[0]
            examname = line[1]
            grade = line[2]
            t.execute(
                "insert into exam(student_ID,examname,grade)values(%s,%s,%s)",
                [student_ID,examname,grade])
            conn.commit()
        else:
            pass

with open("/home/ben/university/student.txt","r") as h:
    while True:
        line = h.readline()
        if line:
            line = line.strip('\n')
            line = line.split(' ')
            print (line)
            ID = line[0]
            name = line[1]
            sex = line[2]
            age = line[3]
            emotion_state = line[4]
            dept_name = line[5]
            t.execute(
                "insert into student(ID,name,sex,age,emotion_state,dept_name)values(%s,%s,%s,%s,%s,%s)",
                [ID,name,sex,age,emotion_state,dept_name])
            conn.commit()
        else:
            pass



# t.execute("select * from student")
# t.execute("select * from exam")
# t.execute("select * from department")

conn.commit()
t.close()
conn.close()
