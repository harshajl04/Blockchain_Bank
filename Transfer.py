import Bank as b
def trans(ANOR,NOR,ANOS,NOS,amount,TID):
    try:
        from datetime import date
        import mysql.connector as m 
        db=m.connect(host='localhost',
                    user='root',
                    passwd='45924572',
                    database='bank_of_kv')
        cur=db.cursor()
        a="select balance from account where Acc_No_=%s"
        cur.execute(a%(ANOS))
        b=cur.fetchone()
        x=int(b[0])
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

trans(435330808,'Harsh',414584475,'Mukesh',5000000,b.TID())


    