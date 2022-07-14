import Bank as ba
def menu():
    print('----Disclaimer----\nPlease Enter Your Account Details Carefully\nFormat Of Date is:yyyy-mm-dd')
    ch=input('----WELCOME TO THE BANK----\n1.Deposit\n2.Withdrawl\n3.Transfer\
        \n4.Statement\n5.History\n6.Exit\nEnter Your Choice:')
    while ch!='6':
        if ch=='1':
            w=int(input('Enter your account number:'))
            x=input('Enter Your Name:')
            y=int(input('Enter amount to deposit:'))
            z=ba.TID()
            ba.depo(w,x,y,z)
        elif ch=='2':
            w=int(input('Enter your account number:'))
            x=input('Enter Your Name:')
            y=int(input('Enter amount to withdraw:'))
            z=ba.TID()
            ba.withd(w,x,y,z)
        elif ch=='3':
            p=int(input('Enter account number of reciever:'))
            q=input("Enter Reciever's Name:")
            r=int(input('Enter account number of sender:'))
            s=input("Enter Sender's Name:")
            t=int(input('Enter amount to transfer:'))
            u=ba.TID()
            ba.trans(p,q,r,s,t,u)
        elif ch=='4':
            p=int(input('Enter your account number:'))
            ba.stmnt(p)
        elif ch=='5':
            p=int(input('Enter your account number:'))
            q=input('Enter Starting Date:')
            r=input('Enter Ending Date:')
            s=int(input('How may transactions do you want to see:'))
            ba.his(p,q,r,s)
        else:
            print('Invalid Input')
        ch=input('----WELCOME TO THE BANK----\n1.Deposit\n2.Withdrawl\n3.Transfer\
        \n4.Statement\n5.History\n6.Exit\nEnter Your Choice:')
    print('Thank you for using our Bank\n We serve the best')

print("----Disclaimer----\nPlease Enter Your Account Details Carefully\nFormat Of Date is:yyyy-mm-dd")
ch=input("----WELCOME TO THE BANK----\n1.Create Account\n2.Login\n3.Exit\nEnter your choice:")
while ch!='3':
    if ch=='1':
        ba.cracc()
        menu()
    elif ch=='2':
        print("Please Enter Your Login Details")
        a=input("Enter Account Number:")
        b=input("Enter Username:")
        c=input("Enter Password:")
        x=ba.login(a,b,c)
        if x==1:
            menu()
    else:
            print("This account is invalid \nPlease check the details you have entered")
    ch=input("----WELCOME TO THE BANK----\n1.Create Account\n2.Login\n3.Exit\nEnter your choice:")


