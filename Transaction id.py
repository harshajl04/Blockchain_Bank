

def TID():
    import random as r
    import string as s
    import mysql.connector as m 
    db=m.connect(host='localhost',
                 user='root',
                 passwd='45924572',
                 database='bank_of_kv')
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
TID()
            


    


    
