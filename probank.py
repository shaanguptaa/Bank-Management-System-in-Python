# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 21:32:24 2020

@author: Sahil

Project: Bank Management System

Language: Python
"""

from random import randint  # library used for generating account number


ACCOUNTS = list()  # creating a list to store accounts

# Inserting Default Accounts in the form of dictionary into the list
ACCOUNTS.append({'accno': 1001,'name': 'ALLEN', 'bal': 1000.00, 'add': 'NEW YORK'})
ACCOUNTS.append({'accno': 1002,'name': 'AKIRA', 'bal': 2500.00, 'add': 'DELHI'})
ACCOUNTS.append({'accno': 1003,'name': 'TIGER', 'bal': 5000.00, 'add': 'MUMBAI'})
ACCOUNTS.append({'accno': 1004,'name': 'BARRY', 'bal': 7500.00, 'add': 'LONDON'})


# mainmenu() funnction
def mainmenu():
    """ Display the main menu """
    choice = -1
    while choice != 8:
        clrscr()
        print('Welcome to Bank Management System')
        print()
        print('1. Create New Account')
        print('2. Deposit Amount')
        print('3. Withdraw Amount')
        print('4. Search An Account')
        print('5. All Account Holder\'s List')
        print('6. Update An Account')
        print('7. Close An Account')
        print('8. Exit')
        print()
        
        choice = int(input('Select Your Option(1-8) : '))
        
        if choice == 1:
            clrscr()
            createAccount()
        elif choice == 2:
            clrscr()
            deposit()
        elif choice == 3:
            clrscr()
            withdraw()
        elif choice == 4:
            clrscr()
            searchAccount()
        elif choice == 5:
            clrscr()
            displayAccounts()
        elif choice == 6:
            clrscr()
            updateAccount()
        elif choice == 7:
            clrscr()
            deleteAccount()
        elif choice == 8:
            pass
        else:
            print('Invalid Option !!!')
            print('Please Select A Valid Option')
            print()
            input('Press Enter To Continue...')



# createAccount() function
def createAccount():
    """ create a new account """
    name = input('Enter Your Name : ').upper()
    address = input('Enter Your Address : ').upper()
    accno = randint(1005, 9999)
    ACCOUNTS.append({'accno': accno,'name': name, 'bal': 0.00, 'add': address})
    print()
    print('Account Created')
    print()
    print('Account No. : ', accno)
    print('Account Holder Name : ', name)
    print('Balance : 0.00 Rs')
    print('Address : ', address)
    print()
    input('Press Enter To Continue')
    

# deposit() function
def deposit():
    """ deposit amount """
    accno = int(input('Enter account no. : '))
    index = search(accno = accno)
    if index is not None:
        print('Account Details : ')
        print('Account No. : ', ACCOUNTS[index].get('accno'))
        print('Account Holder Name : ', ACCOUNTS[index].get('name'))
        bal = ACCOUNTS[index].get('bal')
        print('Balance : ', bal)
        print()

        while True:
            try:
                amount = float(input('Enter The Amount To Deposit : '))
                break
            except ValueError:
                print('Invalid Amount !!!')
                print('Please Enter Valid Amount')
                print()

        ACCOUNTS[index].update({'bal': bal + amount})
        print()
        print(amount, ' Rs Deposited To The Account')
        print('Total Available Balance is : ', ACCOUNTS[index].get('bal'))
    else:
        print()
        print('Account Does Not Exists...')
    print()
    input('Press Enter To Continue')



# withdraw() function
def withdraw():
    """ withdraw amount """
    accno = int(input('Enter account no. : '))
    index = search(accno = accno)
    if index is not None:
        print('Account Details : ')
        print('Account No. : ', ACCOUNTS[index].get('accno'))
        print('Account Holder Name : ', ACCOUNTS[index].get('name'))
        bal = ACCOUNTS[index].get('bal')
        print('Balance : ', bal)
        print()

        while True:
            try:
                amount = float(input('Enter The Amount To Withdraw : '))
            except ValueError:
                print('Invalid Amount !!!')
                print('Please Enter Valid Amount')
                print()
                continue

            if bal >= amount:
                ACCOUNTS[index].update({'bal': bal - amount})
                print()
                print(amount, ' Rs Withdrawen From The Account')
                print('Total Available Balance is : ', ACCOUNTS[index].get('bal'))
                print()
                input('Press Enter To Continue')
                break
            else:
                print('Insufficient Balance !!!')
                choice = input('Do You Want To Withdraw Another Sum Of Amount (y/n)').lower()
                if choice.startswith('n'):
                    break
    else:
        print()
        print('Account Does Not Exists...')
        print()
        input('Press Enter To Continue')

 

# searchAccount() function
def searchAccount():
    """ search for an account and print the details """
    term = input('Enter Account No. or Account Holder\'s Name : ')
    try:
        accno = int(term)
        index = search(accno = accno)
    except ValueError:
        index = search(name = term.upper())
    if index is not None:
        print('Account No. : ', ACCOUNTS[index].get('accno'))
        print('Account Holder\'s Name : ', ACCOUNTS[index].get('name'))
        print('Balance : ', ACCOUNTS[index].get('bal'))
        print('Address : ', ACCOUNTS[index].get('add'))
    else:
        print('Account Not Found')
    print()
    input('Press Enter To Continue')


# search() function
def search(accno = None, name = None):
    """ search for an account and return the index of the account """
    index = -1
    if name is None:
        for acc in ACCOUNTS:
            index += 1
            if acc.get('accno') == accno:
                return index
    elif accno is None:
        for acc in ACCOUNTS:
            index += 1
            if acc.get('name') == name:
                return index
    return None



# displayAccounts() function
def displayAccounts():
    """ display the list of all the account holders """
    srno = 1
    print('SR. NO.  | ACCOUNT NO. \t | ACCOUNT HOLDER\'s NAME')
    for acc in ACCOUNTS:
        print(srno, '\t |', acc['accno'], '\t |', acc['name'])
        srno += 1
    input('Press Enter To Continue')
    


# updateAccount() function
def updateAccount():
    """ update or modify the details of the account """
    term = input('Enter Account No. or Account Holder\'s Name : ')
    try:
        accno = int(term)
        index = search(accno = accno)
    except ValueError:
        index = search(name = term.upper())
    if index is not None:
        print('Account No. : ', ACCOUNTS[index].get('accno'))
        print('Account Holder\'s Name : ', ACCOUNTS[index].get('name'))
        print('Balance : ', ACCOUNTS[index].get('bal'))
        print('Address : ', ACCOUNTS[index].get('add'))
        print()
        print()
        print('1. Update Account Holder\'s Name')
        print('2. Update Address')
        print()
        choice = int(input('Select Your Option : '))
        if choice == 1:
            name = input('Enter New Name : ').upper()
            ACCOUNTS[index].update({'name': name})
            print()
            print('Name Updated Successfully To ', name)
        elif choice == 2:
            address = input('Enter New address : ').upper()
            ACCOUNTS[index].update({'add': address})
            print()
            print('Address Updated Successfully To ', address)
    else:
        print('Account Not Found')
    print()
    input('Press Enter To Continue')



# deleteAccount() function
def deleteAccount():
    """close or delete an account"""
    accno = int(input('Enter Account No. : '))
    index = search(accno = accno)
    if index is not None:
        name = input('Enter Account Holder\'s Name : ').upper()
        if ACCOUNTS[index].get('name') == name:
            ACCOUNTS.pop(index)
            print()
            print('Account Deleted Successfully')
            print()
            input('Press Enter To Continue')
        else:
            print()
            print('Account Does Not Exists !!!')
            input('Press Enter To Continue')
    else:
        print()
        print('Account Does Not Exists !!!')
        input('Press Enter To Continue')



# clrscr() function
def clrscr():
    """ clear the screen by inserting 20 new lines """
    print('\n' * 20)
    
#starting the program by calling the mainmenu() function
mainmenu()
