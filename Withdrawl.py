from datetime import date
from Bank import TID

def withd(AcNo,name,amount,TID):
    
    from datetime import date
    import mysql.connector as m 
    db=m.connect(host='localhost',
                user='root',
                passwd='45924572',
                database='bank_of_kv')
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
        print('Your Account No.:',AcNo,'\nYour current balance is',x-amount,'\nTransaction ID:',TID)
        db.commit()
    else:
        print('Your account has insufficient balance.')
    
withd(414584475,'Mukesh',25000,TID())
        

'''def withd(ID, Amount):
    s="Select money from Table where Bid==ID"
    a=cur.execute()
    if amout > a:
        b="update table set money=money-a where Bid=ID"
        cur.execute(b)
        print('Your balance is:', a-amount)
    else:
        print("Your account doesn't have enough money")'''




        
