###Note-: do download and keep bank.ico file from files... or if u dont wanna use just delete the '''wm_iconbitmap('bank.ico')'''' from every three place
from re import T
from tkinter import *
# from turtle import down
import tkinter.messagebox as tmsg
import pickle 
import datetime as dt
import time 
import os
from turtle import down
import sys




def clear():
           text.delete(1.0, END)

def exite():
    sys.exit()



cust_balance={'Rohan':5000000}
cust_lis=['Rohan']
cust_lis_pass={'Rohan':'123456'}


def admingui(name):
    def clearss():
        textss.delete(1.0,END)
    def show_cust_name():
        if cust_lis==[]:
            textss.delete(1.0, END)
            textss.insert(END,'There are no Customers available')
            tmsg.showinfo("Details","There is no Registration of Customer in Bank.")

        else:
            textss.delete(1.0, END)
            textss.insert(END,'The Customers Names are-:')
            for name in cust_lis:
                textss.insert(END, name + ' , ')
    def show_cust_name_pass():
        if cust_lis==[]:
            textss.delete(1.0, END)
            textss.insert(END,'There are no Customers available')
            tmsg.showinfo("Details","There is no Registration of Customer in Bank.")
        else:
            for i in cust_lis_pass:
                textss.delete(1.0, END)
            textss.insert(END,'')
            for names in cust_lis_pass:
                textss.insert(END, f'LOGIN NAME IS-: {names} and PIN is-: {cust_lis_pass[names]} \n' + ' , ')
    def quitss():
        mains.destroy()

    mains=Tk()
    mains.geometry('1000x700')
    mains.wm_iconbitmap('bank.ico')
    mains.configure(background="lightblue")
    mains.title("Logged in ADMIN")
    mains.maxsize(1000,700)
    mains.minsize(1000,700)
    Label(mains,text=f"Welcome ADMIN {name} in your Account-:",font="algerian 30 bold",fg='black').pack()
    Label(mains,text=f"You are SuccessFully Logged In",fg='black').pack()
    textss=Text(mains, width=50, height=10)
    textss.pack()

    Button(mains,text="CLEAR",command=clearss,borderwidth=5).pack(padx=5,pady=5)

    # # Button(mains,text="LOG OFF",command=main.quit,borderwidth=5,padx=5,pady=5).pack(padx=15,pady=35)
    ff1=Frame(mains,bg='grey',borderwidth=6)
    ff1.pack(side=LEFT,padx=5,pady=5)

    Button(ff1,text="VIEW Customers",borderwidth=10,command=show_cust_name).pack(padx=5,pady=5)

    ff1=Frame(mains,bg='grey',borderwidth=6)
    ff1.pack(side=LEFT,padx=5,pady=5)

    Button(ff1,text="VIEW Customers Login ID",borderwidth=10,command=show_cust_name_pass).pack(padx=5,pady=5)
    Button(mains,text="LOGOUT",borderwidth=10,command=quitss).pack(padx=5,pady=5)


    mains.mainloop()





def newgui(name):
    main=Tk()
    def show_balance():
        name=namess_value.get()
        name=name.title()
        texts.delete(1.0, END)
        texts.insert(END,f'{name} Your Current Balance is {cust_balance[name]} ₹')
        
    def depositss():
        name=namess_value.get()
        name=name.title()
        
        a=ruppees_entry.get()
        if a=='':
            tmsg.showerror('Error',"Kindly ENter Number")
            return 
        a=int(a)
        if a<0 : 
            tmsg.showerror("Error","Kindly ENter a Valid Number")
            return
        cust_balance[name]+=a
        texts.delete(1.0, END)
        texts.insert(END,f'Deposited {a} ₹ in Your Account {name}.')
        with open(f"{name}_transactions_details.txt",'a') as f:
            f.write(f"{a} Ruppees has been Deposited in Your Account On {dt.datetime.now()}\n .")
    def withdraw_bal():
        name=namess_value.get()
        name=name.title()
        a=ruppeess_entry.get()
        if a=='':
        # Checking if the number entered is less than 0. If it is, it will show an error message.
            tmsg.showerror('Error',"Kindly ENter Number")
            return
        a=int(a)
        
        if a<0 : 
            tmsg.showerror("Error","Kindly ENter a Valid Number")
            return
        if a>cust_balance[name]:
            tmsg.showerror("Error","Amount U Entered Is Greater Than U have in Account :)")
            return
        else:
            cust_balance[name]-=a
            texts.delete(1.0, END)
            texts.insert(END,f'{a} ₹ Withdrawn from Your Account. Your current Balance in Account is {cust_balance[name]} ₹.')
            with open(f"{name}_transactions_details.txt",'a') as f:
                f.write(f"{a} ruppees has been WithDrawn From Your Account On {dt.datetime.now()}\n")
    def quitssssss():
        
        texts.delete(1.0, END)
        texts.setvar('LOGGING OUT PLZ WAIT.....')
        texts.insert(END,f'logging out from account {name} .......')
        # time.sleep(3)
        main.destroy()

    def see_tranacation_details():
        if os.path.exists(f"{name}_transactions_details.txt"):
                    
                    
       
            texts.delete(1.0, END)
            with open(f"{name}_transactions_details.txt",'r')as f:
                
                for i in f.readlines():
                    texts.insert(END,f'{i}')
        else:
            tmsg.showerror("Error","File Does not Exist.. first kindly make some Transactions.")

    def delete_transaction_details():
            if os.path.exists(f"{name}_transactions_details.txt"):
                os.remove(f"{name}_transactions_details.txt")
                text.insert(END,"File Deleted")
            else:
                tmsg.showerror('Error',"File Does Not Exist .")



    def change_passssss():
        name=namess_value.get()
        name=name.title()
        a=new_pass_entry.get()
        
        if a=='':
            tmsg.showerror("Error",'Kindly Enter Something')
            return
        if a==cust_lis_pass[name]:
            tmsg.showerror("Error","Enter New Pin ,Not as same as Old")
            return 
        else:
            cust_lis_pass[name]=a
            texts.delete(1.0, END)
            texts.insert(END,f'{name} Your Pin Has Been SuccessFully Changed.')
            tmsg.showinfo("Changed PIN",f'{name} Your PIN has Been SuccessFully Changed')
            with open(f"{name}_transactions_details.txt",'a') as f:
                f.write(f"{name} You Have Changed Your Password on {dt.datetime.now()}\n")

    main.geometry('1000x700')
    main.wm_iconbitmap('bank.ico')
    main.configure(background="lightblue")
    main.title("Logged in")
    Label(main,text=f"Welcome {name} in your Account-:",font="algerian 30 bold",fg='black').pack()
    Label(main,text=f"You are SuccessFully Logged In",fg='black').pack()
    main.maxsize(1000,700)
    main.minsize(1000,700)
    def clears():
        texts.delete(1.0,END)

    texts=Text(main, width=50, height=10)
    texts.pack()
    ff1=Frame(main,bg='grey',borderwidth=6)
    ff1.pack(side=LEFT,padx=5,pady=5)

    Button(ff1,text="VIEW BALANCE",borderwidth=10,command=show_balance).pack(padx=5,pady=5)
    ff3=Frame(main,bg='grey',borderwidth=6)
    ff3.pack(side=LEFT,padx=5,pady=5)
    lx=Label(ff3,text='Enter Amount to Withdraw-:').pack(padx=5,pady=5)

    ruppeess_value=StringVar()
    

    ruppeess_entry=Entry(ff3,textvariable=ruppeess_value)
    ruppeess_entry.pack(padx=5,pady=5)
    Button(ff3,text="WITHDRAW",borderwidth=10,command=withdraw_bal).pack(padx=5,pady=5)
    ff2=Frame(main,bg='grey',borderwidth=6)
    ff2.pack(side=LEFT,padx=5,pady=5)
    lx=Label(ff2,text='Enter Amount to Deposit-:').pack(padx=5,pady=5)

    ruppees_value=IntVar()
    

    ruppees_entry=Entry(ff2,textvariable=ruppees_value)
    ruppees_entry.pack(padx=5,pady=5)
    Button(ff2,text="DEPOSIT",borderwidth=10,command=depositss).pack(padx=5,pady=5)

    ff4=Frame(main,bg='grey',borderwidth=6)
    ff4.pack(side=LEFT,padx=5,pady=5)
    lx=Label(ff4,text='Enter New Pin to Set-:').pack(padx=5,pady=5)

    new_pass_value=StringVar()
    
    new_pass_entry=Entry(ff4,textvariable=new_pass_value)
    new_pass_entry.pack(padx=5,pady=5)
    Button(ff4,text="Change Pin-:",borderwidth=10,command=change_passssss).pack(padx=5,pady=5)

    ff5=Frame(main,bg='grey',borderwidth=6)
    ff5.pack(side=LEFT,padx=5,pady=5)
    

    
    new_pass_entry.pack(padx=5,pady=5)
    Button(ff5,text="SHOW TRANSACTION DETAILS",borderwidth=10,command=see_tranacation_details).pack(padx=5,pady=5)

    


    Button(main,text="CLEAR",command=clears,borderwidth=5).pack()
    Button(main,text="LOGOUT",command=quitssssss,borderwidth=5,padx=5,pady=5).pack(padx=15,pady=35)
    # ff6=Frame(main,bg='grey',borderwidth=6)
    # ff6.pack(padx=5,pady=5)
    

    
    # new_pass_entry.pack(padx=5,pady=5)
    Button(main,text="DELETE TRANS",borderwidth=10,command=delete_transaction_details).pack(side=BOTTOM,padx=5,pady=5)
    main.mainloop()
hr={'Rvc':'123456'}
# # # # # newgui('Rohan')

        




def customer():
    if name_value.get()=='' or password_value.get()=='':
        tmsg.showerror("Error","Kindly Fill Name and Password")
        return
    name=name_value.get()
    name=name.title()
    if name in cust_lis:
        tmsg.showerror("Error",f"Account name with {name} Already Exist. Kindly Choose Another Name")
        return
    else:
        file='cust_lis.pkl'
        files='cust_balance.pkl'
        filess='cust_lis_pass.pkl'

        with open(file,'wb') as f:
            pickle.dump(cust_lis,f)

        with open(filess,'wb') as f:
            pickle.dump(cust_lis_pass,f)

        with open(files,'wb') as f:
            pickle.dump(cust_balance,f)

        file='cust_lis.pkl'
        with open(file,'rb') as f:
            cust_liss=pickle.load(f)
            pass

        file='cust_lis_pass.pkl'
        with open(filess,'rb') as f:
            cust_lis_passs=pickle.load(f)
            pass

        files='cust_balance.pkl'
        with open(files,'rb') as f:
            cust_balances=pickle.load(f)
            pass
        password=password_value.get()
        cust_lis.append(name)
        cust_lis_pass[name]=password
        cust_balance[name]=0
        

        
        text.delete(1.0, END)
        text.insert(END,f'{name} Account Has Been Created')
        tmsg.showinfo('Account Created',f'{name} Account Created')
        

def cus_login():
    name=namess_value.get()
    name=name.title()
    if name=='' or passwordss_value.get()=='':
        tmsg.showerror("Error","Kindly Fill Name and Password")
        return
    if name in cust_lis:
        if cust_lis_pass[name]==passwordss_value.get():
            tmsg.showinfo("Details",f"SUCCESSULLY LOGGED IN ,press OK to continue")
            text.delete(1.0, END)
            text.insert(END,f'Logged In to {name} Account:')
            newgui(name)
        else:
            tmsg.showerror("Error",f"Wrong Password , Kindly Enter Again")
    else:
        tmsg.showerror("Error",f"No Account Found With Name -: {name}")

def admin_logins():
    name=names_value.get()
    name=name.title()
    if name=='' or passwords_value.get()=='':
        tmsg.showerror("Error","Kindly Fill Name and Password")
        return
    if name in hr:
        if hr[name]==passwords_value.get():
            tmsg.showinfo("Details",f"SUCCESSULLY LOGGED IN ADMIN,press OK to continue")
            text.delete(1.0, END)
            text.insert(END,f'Logged In to ADMIN {name} Account:')
            admingui(name)
        else:
            tmsg.showerror("Error",f"Wrong Password , Kindly Enter Again")
    else:
        tmsg.showerror("Error",f"No ADMIN Account Found With Name -: {name}")










window=Tk()
window.geometry('1000x700')
window.title("Bank Management")
window.wm_iconbitmap('bank.ico')
Label(text="Welcome to RVC BANK",font="algerian 30 bold",fg='black',borderwidth=5,relief=SUNKEN).pack(padx=5,pady=5)
text=Text(window, width=50, height=10)
text.pack()
window.configure(background="lightblue")

# lend_book=Label(text="ADMIN LOGIN-: ").pack()
# return_book=Label(text="RETURN LENDED BOOK").grid(row=4,column=1)
# f=Frame(window)
# add_book=Label(f,text="CREATE ACCOUNT (Name & Password)-:").pack()

# add_book_value=StringVar()
# add_book_entry=Entry(f,window,textvariable=add_book_value)
# add_book_entry.pack()
# Button(f,text="Create Account",command=quit).pack()
f1=Frame(window,bg='grey',borderwidth=6)
f1.pack(side=LEFT,padx=5,pady=5)
l=Label(f1,text='Create Account-:',padx=10,pady=10,font='helvatica 14 bold')
l.pack(pady=2)

lx=Label(f1,text='Name & Password').pack(padx=5,pady=5)

name_value=StringVar()
password_value=StringVar()

name_entry=Entry(f1,textvariable=name_value)
name_entry.pack(padx=5,pady=5)
password_entry=Entry(f1,textvariable=password_value)
password_entry.pack(padx=5,pady=5)
Button(f1,text="Create Account",borderwidth=10,command=customer).pack(padx=5,pady=5)

f3=Frame(window,bg='grey',borderwidth=6)
f3.pack(side=LEFT,padx=5,pady=5)
l=Label(f3,text='CUSTOMER LOGIN-:',padx=10,pady=10,font='helvatica 14 bold')
l.pack(pady=2)

lsa=Label(f3,text='Name & Password').pack(padx=5,pady=5)

namess_value=StringVar()
passwordss_value=StringVar()

namess_entry=Entry(f3,textvariable=namess_value)
namess_entry.pack(padx=5,pady=5)
passwordss_entry=Entry(f3,textvariable=passwordss_value)
passwordss_entry.pack(padx=5,pady=5)
Button(f3,text="LOGIN",borderwidth=10,command=cus_login).pack(padx=5,pady=5)

f2=Frame(window,bg='grey',borderwidth=6)
f2.pack(side=LEFT)
l=Label(f2,text='ADMIN LOGIN-:',padx=10,pady=10,font='helvatica 14 bold')
l.pack(pady=2)

lsa=Label(f2,text='Name & Password').pack(padx=5,pady=5)

names_value=StringVar()
passwords_value=StringVar()




names_entry=Entry(f2,textvariable=names_value)
names_entry.pack(padx=5,pady=5)
passwords_entry=Entry(f2,textvariable=passwords_value)
passwords_entry.pack(padx=5,pady=5)
Button(f2,text="LOGIN",borderwidth=10,command=admin_logins).pack(padx=5,pady=5)
Button(window,text="CLEAR",command=clear,borderwidth=5).pack()
Button(window,text="EXIT",command=exite,borderwidth=5,padx=5,pady=5).pack(padx=15,pady=35)


    


window.maxsize(1000,700)
window.minsize(1000,700)
window.mainloop()
