
from Bank import TID
def depo(AcNo,name,amount,TID):
    from datetime import date
    import mysql.connector as m 
    db=m.connect(host='localhost',
                user='root',
                passwd='45924572',
                database='bank_of_kv')
    cur=db.cursor()
    s="update Account set balance=balance+%s where Acc_No_=%s and Name=%s"
    cur.execute(s,(amount,AcNo,name))    
    s="insert into deposit values ('%s','%s','%s','%s','%s')"
    cur.execute(s%(AcNo,name,date.today(),amount,TID))
    s="select balance from account where Acc_No_=%s and Name='%s'"
    cur.execute(s%(AcNo,name))
    a=cur.fetchone()
    x=int(a[0])
    print('Your Account No.:',AcNo,'\nYour current balance is',x+amount,'\nTransaction ID:',TID)
    db.commit()
depo(414584475,'Mukesh',25000000,TID())


        
