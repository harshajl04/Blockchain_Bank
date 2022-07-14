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
        
def depo(AcNo,name,amount,TID):
    try:
        from datetime import date
        import mysql.connector as m 
        db=m.connect(host='localhost',
                    user='root',
                    passwd='45924572',
                    database='bank')
        cur=db.cursor()
        s="update Account set balance=balance+%s where Acc_No_=%s and Name=%s"
        cur.execute(s,(amount,AcNo,name))    
        s="insert into deposit values ('%s','%s','%s','%s','%s')"
        cur.execute(s%(AcNo,name,date.today(),amount,TID))
        s="select balance from account where Acc_No_=%s and Name='%s'"
        cur.execute(s%(AcNo,name))
        a=cur.fetchone()
        x=int(a[0])
        print('Your Account No.:',AcNo,'\nYour current balance is',x,'\nTransaction ID:',TID)
        db.commit()
    except:
        print('This account is invalid \nPlease check the details you have entered')    

def withd(AcNo,name,amount,TID):
    try:
        from datetime import date
        import mysql.connector as m 
        db=m.connect(host='localhost',
                    user='root',
                    passwd='45924572',
                    database='bank')
        cur=db.cursor()
        a="select balance from account where Acc_No_=%s and Name='%s'"
        cur.execute(a%(AcNo,name))
        b=cur.fetchone()
        x=int(b[0])
        if x>amount:
            s="insert into withdrawl values (%s,%s,%s,%s,%s)"
            cur.execute(s,(AcNo,name,date.today(),amount,TID))
            s="update Account set balance=balance-%s where Acc_No_=%s and Name=%s"
            cur.execute(s,(amount,AcNo,name))
            s="select balance from account where Acc_No_=%s and Name='%s'"
            cur.execute(s%(AcNo,name))
            a=cur.fetchone()
            c=int(a[0])
            print('Your Account No.:',AcNo,'\nYour current balance is',c,'\nTransaction ID:',TID)
            db.commit()
        else:
            print('Your account has insufficient balance.')
    except:
        print('This account is invalid \nPlease check the details you have entered')
        
def trans(ANOR,NOR,ANOS,NOS,amount,TID):
    try:
        from datetime import date
        import mysql.connector as m 
        db=m.connect(host='localhost',
                    user='root',
                    passwd='45924572',
                    database='bank')
        cur=db.cursor()
        a="select name,balance from account where Acc_No_=%s"
        cur.execute(a%(ANOS))
        b=cur.fetchone()
        x=int(b[1])
        if x>amount:
            c="update account set balance=balance-%s where Acc_No_=%s and Name=%s"
            cur.execute(c,(amount,ANOS,NOS))
            d="update account set balance=balance+%s where Acc_No_=%s and Name=%s"
            cur.execute(d,(amount,ANOR,NOR))
            s="select balance from account where Acc_No_=%s and Name='%s'"
            cur.execute(s%(ANOS,NOS))
            a=cur.fetchone()
            print('Your Account No.:',ANOS,'\nYour current balance is',x-amount,'\nTransaction ID:',TID)
            s="insert into transfer values (%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(s,(ANOR,NOR,ANOS,NOS,amount,date.today(),TID))
        else:
            print('Your account has insufficient balance.')
        db.commit()
                 
    except:
        print('This account is invalid \nPlease check the details you have entered')

def TID():
    import random as r
    import string as s
    import mysql.connector as m 
    db=m.connect(host='localhost',
                 user='root',
                 passwd='45924572',
                 database='bank')
    cur=db.cursor()
   
    while True: 
        l=''
        for i in range(30):
            g=r.choice(s.ascii_uppercase+s.digits)
            l+=g
        a="select Transaction_ID from id"
        cur.execute(a)
        y=cur.fetchall()
        if l not in y:
            x="insert into id(transaction_id) values('%s')"%(l)
            cur.execute(x)
            db.commit()
            return l      
        else:
            True

def AID():
    import random as r
    import string as s
    import mysql.connector as m 
    db=m.connect(host='localhost',
                 user='root',
                 passwd='45924572',
                 database='bank')
    cur=db.cursor()
    while True: 
        l=''
        for i in range(9):
            g=r.choice(s.digits)
            l+=g
        a="select Acc_No_ from id"
        cur.execute(a)
        y=cur.fetchall()
        if l not in y:
            x="insert into id(Acc_No_) values('%s')"%(l)
            cur.execute(x)
            db.commit()
            return l   
        else:
            True
    db.commit()

def stmnt(ACNO):
    try:
        import mysql.connector as m 
        db=m.connect(host='localhost',
                    user='root',
                    passwd='45924572',
                    database='bank')
        cur=db.cursor()
        a="select Name,balance from account where Acc_No_=%s"
        cur.execute(a%(ACNO))
        d=cur.fetchone()
        print('Account Number:',ACNO,'\nName:',d[0],'\nBalance:',d[1])
        db.commit()
    except:
        print('This account is invalid \nPlease check the details you have entered')

def his(ACNO,sd,ed,n):
    import datetime
    import mysql.connector as m 
    db=m.connect(host='localhost',
                user='root',
                passwd='45924572',
                database='bank')
    cur=db.cursor()
    try:
        a="create table demo(ANOR int, NOR varchar(20), ANOS int, NOS Varchar(20), Balance int,Date date, TID Varchar(30), DCT varchar(10))"
        cur.execute(a)                        
        s="select * from deposit where %s=Acc_No_ and date>=%s and date <=%s"
        cur.execute(s,(ACNO,sd,ed))
        a=cur.fetchall()
        for i in a:
            x="insert into demo(ANOR,NOR,Date,Balance,TID,DCT) values(%s,%s,%s,%s,%s,%s) "
            cur.execute(x,(i[0],i[1],i[2],i[3],i[4],'Credit'))
        s="select * from withdrawl where %s=Acc_No_ and date>=%s and date <=%s"
        cur.execute(s,(ACNO,sd,ed))
        a=cur.fetchall()
        for i in a:
            x="insert into demo(ANOR,NOR,Date,Balance,TID,DCT) values(%s,%s,%s,%s,%s,%s) "
            cur.execute(x,(i[0],i[1],i[2],i[3],i[4],"Debit"))
        s="select * from transfer where %s=ANOS or %s=ANOR and date>=%s and date <=%s"
        cur.execute(s,(ACNO,ACNO,sd,ed))
        a=cur.fetchall()
        for i in a:
            x="insert into demo(ANOR,NOR,ANOS,NOS,Date,Balance,TID,DCT) values(%s,%s,%s,%s,%s,%s,%s,%s) "
            cur.execute(x,(i[0],i[1],i[2],i[3],i[5],i[4],i[6],'Transfer'))
        s="select * from demo order by date desc"
        cur.execute(s)
        a=cur.fetchall()
        print('ANO(R)','NO(R)','ANOS','NOS','Balacnce','Date','TID','DCT',sep='     ')
        if n>=len(a):
            for i in a:
                print(i)
        else:
            for i in range(n):
                print(a[i])
        db.commit()
    except:
        print('This account is invalid \nPlease check the details you have entered')
    finally:
        s='drop table demo'
        cur.execute(s)
        db.commit() 

def login(ACNO,x,y):
    try:
        import mysql.connector as m 
        db=m.connect(host='localhost',
                    user='root',
                    passwd='45924572',
                    database='bank')
        cur=db.cursor()
        a="select username,password from login where ACNO=%s"
        cur.execute(a%(ACNO))
        d=cur.fetchone()
        if d[0]==x and d[1]==y:
            return 1
        else:
            print("This account is invalid \nPlease check the details you have entered")

        db.commit()
    except:
        print('This account is invalid \nPlease check the details you have entered')
    
    



    
