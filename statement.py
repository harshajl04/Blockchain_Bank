def stmnt(ACNO):
    a='select Name,balance from account where Acc_No_=ACNO'
    cur.execute(a)
    d=cur.fetch()
    print('Account Number:',ACNO,'Name:',d[0],'Balance:',d[1])
