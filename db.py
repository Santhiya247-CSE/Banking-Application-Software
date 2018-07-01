import mysql.connector
from myfunc import *
accno=7600775
custid=1000
choice=-1
while (choice!=0):
        choice =int(input("1.Sign-up\n2.Sign-in\n3.Admin Sign-in\n4.Quit\n"))
        if( choice==1 ):
                fname = input("Enter the first name:")
                lname = input("Enter the Last name:")
                addr = input("Enter address: ")
                street=input("Enter the street name:  ")
                city=input("Enter the city name: ")
                pincode=int(input("Enter the pincode:  "))
                pwd = input("Set a valid Password(maximum 8 characters-combination of alphabets and numbers):")
                acctype = input("Enter the account type:")
                balance=1000
                for i in range(accno,accno+5):
                        accno=i
                acno=accno
                for i in range(custid,custid+5):
                        custid=i
                cid=custid
                SignUp(cid,accno,fname,lname,addr,street,city,pincode,balance,pwd,acctype)
                continue
        if(choice==2):
                cid=input("Customer ID:")
                pwd=input("Password:")
                SignIn(cid,pwd)
                choice2=0
                while (choice2!=4):
                        choice2 = int(input( "Choose:-\n1.Address Change\n2.Open New Account\n3.Deposit\n4.Withdrawal\n5.Transfer Money\n6.Print statement\n7.Account Closure\n8.Avail Loan\n0.Customer Logout\n"))
                        if(choice2==1):
                                naddr=input("Enter address to be changed:")
                                AddrChg(naddr,cid)
                                continue
                        if(choice2==2):
                                acctype=input("Type of account:")
                                newAcc(cid,acctype)
                                continue
                        if(choice2==3):
                                accno=input("Enter Account number:")
                                amt=int(input("Enter the amount to deposit:"))
                                Deposit(amt,accno)
                                continue
                        if(choice2==4):
                                accno=input("Enter Account number:")
                                amt=int(input("Enter the Amount to withdraw:"))
                                Withdraw(amt,accno)
                                continue
                        if(choice2==5):
                                accno=input("Account number to be withdrawn:")
                                accno1=input("Account number to be deposited:")
                                amt=int(input("Amount to be transferred:"))
                                transfer(accno,accno1,amt)
                                continue
                        if(choice2==6):
                                accno=input("Enter the Account number:")
                                printStmt(accno)
                                continue
                        if(choice2==7):
                                accno=input("Account number that has to be closed:")
                                acctClosure(accno)
                                continue
                        if(choice2==8):
                                accno=input("Enter the Account number:")
                                loan(accno)
                                continue
                        if(choice2==0):
                                print ("Thank you! You have been logged out!!! ")
                                break           
                continue
        if( choice==3 ):
                cid=input ("Enter the Admin ID:")
                pwd=input( "Enter the Password: " )
                ASignIn(cid,pwd)
                choice3=0
                while(choice3!=10):
                        choice3=int(input("Enter your choice:\n1.FD report of customer\n2.FD report of customer via another customer\n3.FD report of customer w.r.t particular fd amount\n4.Loan report of a customer\n5.Loan report of customer via another customer\n6.Loan report of a customer w.r.t particular loan amount\n7.Loan-fd report of a customer\n8.Report of customers who are yet to avail a loan\n9.Report of custoemr who are yet to open a fd account\n10.Report a customer who neither have a loan nor fd\n"))
                        if(choice3==1):
                                    cid=input("Enter the customer id:")
                                    listfd(cid)
                                    continue
                        if(choice3==2):
                                    cid=input("Enter the customer id:")
                                    checkfd(cid)
                                    continue
                        if(choice3==3):
                                    amt=input("Enter the FD amount:")
                                    reportfd(amt)
                                    continue
                        if(choice3==4):
                                    accno=input("Enter the account no:")
                                    listloan(accno)
                                    continue
                        if(choice3==5):
                                    cid=input("Enter the customer id:")
                                    checkloan(cid)
                                    continue
                        if(choice3==6):
                                    amt=input("Enter the loan amount:")
                                    reportloan(amt)
                                    continue
                        if(choice3==7):
                                    print("Customer Details:")
                                    lfreport()
                                    continue
                continue
        if( choice==4 ):
                print("Sorry!You've Exited!")
                break


