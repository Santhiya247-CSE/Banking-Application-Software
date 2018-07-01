import mysql.connector
import random
import datetime
def SignUp(cid,accno,fname,lname,addr,street,city,pincode,balance,pwd,acctype):
        db=mysql.connector.connect(user='root',password='pinkysan',database='module5')
        curs=db.cursor()
        sql="insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        args=(cid,accno,fname,lname,addr,street,city,pincode,balance,pwd,acctype)
        curs.execute(sql,args)
        print("Inserted Successfully!")
        db.commit()
        db.close()
        return

def SignIn(cusid,pwd):
        db=mysql.connector.connect(user='root',password='pinkysan',database='module5')
        curs=db.cursor()
        count=1
        while(count!=3):
                sql="select pwd from customer where cid='%s'"%(cusid)
                #args=cusid
                curs.execute(sql)
                result=curs.fetchone()
                print(result[0])
                if (result[0]==pwd):
                        print("You have successfully logged in")
                        break
                else:
                        print("Password incorrect :(")
                        count=count+1
                        pwd=input("Re-Enter Password")
        db.commit()
        db.close()
        return;

def ASignIn(adid,pwd):
        db=mysql.connector.connect(user='root',password='pinkysan',database='module5')
        curs=db.cursor()
        count=0
        while(count!=3):
                sql="select pwd from bank where adid='%s'"%(adid)
                curs.execute(sql)
                result=curs.fetchone()
                if(result[0]==pwd):
                        print("You have successfully logged in")
                        break
                else:
                        print("Password incorrect :(")
                        count=count+1
                        pwd=input("Re-Enter Password")
        db.close()
        return;

def AddrChg(newaddr,custid):
        db=mysql.connector.connect(user='root',password='pinkysan',database='module5')
        curs=db.cursor()
        sql="update customer set addr='%s' where cid='%s'"
        args=(newaddr,custid)
        curs.execute(sql,args)
        print("Address updated successfully")
        db.commit()
        db.close()
        return;

def Deposit(amt,acctno):
        db=mysql.connector.connect(user='root',password='pinkysan',database='module5')
        curs=db.cursor()
        sql1="select balance from customer where accno='%s'"%(acctno)
        curs.execute(sql1)
        bal=curs.fetchone()
        bal1=int(bal[0])+amt
        sql="update customer set balance='%s' where accno='%s'"%(bal1,acctno)
        curs.execute(sql)
        sql="insert into deposit values(%s,%s,%s)"
        now=datetime.datetime.now().strftime("%Y-%m-%d")
        dod=str(now)
        args=(acctno,amt,dod)
        curs.execute(sql,args)
        print("Balance credited successfully")
        db.commit()
        db.close()
        return;  

def Withdraw(amt,acctno):
        db=mysql.connector.connect(user='root',password='pinkysan',database='module5')
        curs=db.cursor()
        sql1="select balance from customer where accno='%s'"%(acctno)
        curs.execute(sql1)
        bal=curs.fetchone()
        if(bal[0]>1000):
                bal1=int(bal[0])-amt
                sql="update customer set balance='%s' where accno='%s'"%(bal1,acctno)
                curs.execute(sql)
                sql="insert into withdrawal values(%s,%s,%s)"
                now=datetime.datetime.now().strftime("%Y-%m-%d")
                dod=str(now)
                args=(acctno,amt,dod)
                print("Money Withdrawn successfully")
        else:
                print("Exceeded Minimum Balance")
        db.commit()
        db.close()
        return
def newAcc(custid,acctype):
        db=mysql.connector.connect(user='root',password='pinkysan',database='module5')
        curs=db.cursor()
        #if(acctype=='saving')
        #if(acctype=='current')
        if(acctype=='fixed'):
                amt=int(input("Enter the amount to be deposited:"))
                depot=int(input("Enter the deposit terms in month"))
                sql="insert into fd values(%s,%s,%s)"%(custid,amt,depot)
                curs.execute(sql)
        print("Account created successfully!!!")
        db.commit()
        db.close()
def transfer(acctno,acctno1,amt):
        db=mysql.connector.connect(user='root',password='pinkysan',database='module5')
        curs=db.cursor()
        sql1="select balance from customer where accno='%s'"%(acctno)
        curs.execute(sql1)
        bal=curs.fetchone()
        if(int(bal[0])>amt):
                Withdraw(amt,acctno)
                Deposit(amt,acctno1)
                print("Amount transferred successfully!!")
        else:
                print("Sorry! Insufficient balance... :/")
        db.commit()
        db.close()

def printStmt(accno):
        db=mysql.connector.connect(user='root',password='pinkysan',database='module5')
        curs=db.cursor()
        print("Account Number : "+ accno)
        sql1="select * from deposit where accno='%s'"%(accno)
        curs.execute(sql1)
        row = curs.fetchone() 
        while row is not None:
            print("Date:",row[2])
            print("Amount:",row[1])
            row = curs.fetchone()
        sql1="select * from withdraw where accno='%s'"%(accno)
        curs.execute(sql1)
        row = curs.fetchone() 
        while row is not None:
            print(row['dow']+" DEBIT "+row['amt'])
            row = curs.fetchone()
        db.commit()
        db.close()

def acctClosure(accno):
        db=mysql.connector.connect(user='root',password='pinkysan',database='module5')
        curs=db.cursor()
        sql1="delete from customer where accno='%s'"%(accno)
        curs.execute(sql1)
        print("Deleted Successfully!")
        sql1="insert into closure values(%s,%s)"
        now=datetime.datetime.now().strftime("%Y-%m-%d")
        doc=str(now)
        args=(accno,doc)
        curs.execute(sql1,args)
        db.commit()
        db.close()
                
def loan(accno):
        db=mysql.connector.connect(user='root',password='pinkysan',database='module5')
        curs=db.cursor()
        #a=2
        amt=int(input("Enter the loan amount:"))
        #sql1=("select balance from customer where acctype='savings' and accno='%s'")%(accno)
        #curs.execute(sql1)
        #row=curs.fetchone()
        #result=int(row[0])*int(a)
        repayt=int(input("Enter the repayment terms in month:"))
        #if(amt > result):
        sql="insert into loan values(%s,%s,%s)"%(accno,amt,repayt)
         #args=(accno,amt,repay)
        curs.execute(sql)
        print("Loan granted successfully")
        db.commit()
        db.close()
def listfd(cid):
        db=mysql.connector.connect(user='root',password='pinkysan',database='module5')
        curs=db.cursor()
        sql="select cid from customer where cid='%s'"%(cid)
        curs.execute(sql)
        result=curs.fetchone()
        if(result[0]=='NULL'):
                print("Customer id  not matched")
        sql="select * from fd where custid='%s'"%(cid)
        curs.execute(sql)
        result=curs.fetchone()
        print("customer id  :",result[0])
        print("amount  :",result[1])
        print("Deposit in terms  :",result[2])
        db.commit()
        db.close()
def checkfd(cid):
        db=mysql.connector.connect(user='root',password='pinkysan',database='module5')
        curs=db.cursor()
        sql="select cid from customer where cid='%s'"%(cid)
        curs.execute(sql)
        result=curs.fetchone()
        #if(result[0]=='NULL'):
        #       print("Customer id  not matched")
        sql="select * from fd where amt >(select sum(amt) from fd where custid='%s')"%(cid)
        curs.execute(sql)
        result=curs.fetchone()
        print("customer id  :",result[0])
        print("amount  :",result[1])
        print("Deposit in terms  :",result[2])
        db.commit()
        db.close()
def reportfd(amt):
        db=mysql.connector.connect(user='root',password='pinkysan',database='module5')
        curs=db.cursor()
        sql="select c.cid,c.fname,c.lname,f.amt from customer c INNER JOIN fd f on c.cid=f.custid where amt>'%s'"%(amt)
        curs.execute(sql)
        result=curs.fetchall()
        count=curs.rowcount
        print(count)
        for row in result:
                print("customer id  :",row[0])
                print("First name :",row[1])
                print("Last name  :",row[2])
                print("Amount:",row[3])
        db.commit()
        db.close()
def listloan(accno):
        db=mysql.connector.connect(user='root',password='pinkysan',database='module5')
        curs=db.cursor()
        sql="select cid from customer where accno='%s'"%(accno)
        curs.execute(sql)
        result=curs.fetchone()
        if(result[0]=='NULL'):
                print("Customer id  not matched")
        sql="select * from loan where accno='%s'"%(accno)
        curs.execute(sql)
        result=curs.fetchone()
        print("Customer id  :",result[0])
        print("Account no:",result[1])
        print("amount  :",result[2])
        print("Repayment in terms  :",result[3])
        db.commit()
        db.close()
def checkloan(cid):
        db=mysql.connector.connect(user='root',password='pinkysan',database='module5')
        curs=db.cursor()
        sql="select cid from customer where cid='%s'"%(cid)
        curs.execute(sql)
        result=curs.fetchone()
        #if(result[0]=='NULL'):
        #       print("Customer id  not matched")
        sql="select * from loan where amt >(select sum(amt) from loan where cid='%s')"%(cid)
        curs.execute(sql)
        result=curs.fetchone()
        print("customer id  :",result[0])
        print("Account no:",result[1])
        print("amount  :",result[2])
        print("Repayment in terms of month :",result[3])
        db.commit()
        db.close()
def reportloan(amt):
        db=mysql.connector.connect(user='root',password='pinkysan',database='module5')
        curs=db.cursor()
        sql="select c.cid,c.fname,c.lname,l.amt from customer c INNER JOIN loan l on c.cid=l.cid where amt>'%s'"%(amt)
        curs.execute(sql)
        result=curs.fetchall()
        count=curs.rowcount
        print(count)
        for row in result:
                print("customer id  :",row[0])
                #print("Account no:",row[1])
                print("First name :",row[1])
                print("Last name  :",row[2])
                print("Amount:",row[3])
        db.commit()
        db.close()
def lfreport():
         db=mysql.connector.connect(user='root',password='pinkysan',database='module5')
         curs=db.cursor()
         sql="select c.cid,c.fname,c.lname from customer c INNER JOIN loan l INNER JOIN fd f on c.cid=l.cid and c.cid=f.custid where l.amt>f.amt"
         curs.execute(sql)
         result=curs.fetchall()
         for row in result:
                 print("CUSTOMER ID:",row[0])
                 print("FIRST NAME:",row[1])
                 print("LAST NAME:",row[2])
                 print("SUM OF LOAN AMOUNT",row[3])
                 print("SUM OF FIXED DEPOSIT AMOUNT:",row[4])
         db.commit()
         db.close()
