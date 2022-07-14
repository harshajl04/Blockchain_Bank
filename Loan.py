def loan(Acc_No,Name,amount):
    import Bank as b
    from datetime import date
    import mysql.connector as m 
    db=m.connect(host='localhost',
                 user='root',
                 passwd='45924572',
                 database='bank_of_kv')
    cur=db.cursor()

    b='Insert into loan values(%s,%s,%s,%s,%s)'
    cur.execute(b,(Acc_No_,Name,Amount,date.today(),b.TID()))
    a=p*((1+((r/n)/100))**(t*n))


    