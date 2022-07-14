def his(ACNO,sd,ed,n):
    import mysql.connector as m 
    db=m.connect(host='localhost',
                user='root',
                passwd='45924572',
                database='bank_of_kv')
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
        s="select * from transfer where %s=ANOS and date>=%s and date <=%s"
        cur.execute(s,(ACNO,sd,ed))
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

    

his(414584475,'2020-12-18','2020-12-24',20)
    
    
