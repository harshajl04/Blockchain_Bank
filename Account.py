
def cracc():
    import Bank as b
    import mysql.connector as m 
    db=m.connect(host='localhost',
                 user='root',
                 passwd='45924572',
                 database='bank')
    cur=db.cursor()
    s1=b.AID()
    s2=input('Enter Your Name:')
    s3=input("Enter Your Father's Name:")
    s4=input("Enter Your Mother's Name:")
    s5=input("Enter Your D.O.B:")
    s6=int(input("Enter Your Opening Amount:"))
    s7=input("Username:")
    s8=input("Password:")
    cr="insert into login(ACNO,username,password) values(%s,%s,%s)"
    cur.execute(cr,(s1,s7,s8))
    cr="insert into account(Acc_No_,Name,Father_name,mother_name,dob,balance) values(%s,%s,%s,%s,%s,%s)"
    val=(s1,s2,s3,s4,s5,s6)
    cur.execute(cr,val)
    print('Your Account No.:',s1,'\nYour Name:',s2,'\nBalance:',s6)
    db.commit()
cracc()
