def AID():
    import random as r
    import string as s
    
    while True: 
        l=''
        for i in range(9):
            g=r.choice(s.digits)
            l+=g
        
        a="select Acc_No_ from id"
        cur.execute(a)
        y=fetchall()
        if l not in y:
            x='insert into id(Acc_no_) values(l)'
            return l
            break   
        else:
            True