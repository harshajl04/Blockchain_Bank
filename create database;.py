import mysql.connector as m 
db=m.connect(host='localhost',
            user='root',
            passwd='45924572',
            database='bank')
cur=db.cursor()
cr="""create table account(
Acc_No_ int Primary key,
Name varchar(25),
Father_Name varchar(25),
Mother_Name varchar(25),
DOB date,
Balance int
);
create table deposit(
Acc_No_  int,
Name varchar(25),
Date date,
Amount int,
Transaction_ID varchar(30),
foreign key (Acc_No_) references Account(Acc_No_)
);
create table Withdrawl(
Acc_No_  int,
Name varchar(25),
Date date,
Amount int,
Transaction_ID varchar(30),
foreign key (Acc_No_) references Account(Acc_No_)
);
create table Transfer(
ANOR int,
NOR varchar(25),
ANOS int,
NOS  varchar(25),
Amount int(12),
Date date,
Transaction_ID varchar(30),
foreign key (ANOR) references Account(Acc_No_),
foreign key (ANOS) references Account(Acc_No_)
);
create table id(
Transaction_ID varchar(30),
Acc_No_ int
);
create table login(
ACNO int,
username varchar(25),
password varchar(25) default 123456
);"""
cur.execute(cr,multi=True)
db.commit()
                                                                                                                                    



