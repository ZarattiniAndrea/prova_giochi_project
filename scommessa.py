from enum import Enum
import random
balance = 1000
    
def main():
    global balance
    print("Ciao, Benvenuto allo Scommettitore brutto figlio di puttana")
    fine = 1
    while fine != -1:
        scom = bet()
        sum = rolldice()
        if sum == 7 or sum == 11:
            print("HAI VINTO!\n")
            balance = balance + scom
            print("SALDO: ",balance)
        elif sum == 2 or sum == 3 or sum == 12: 
            print("HAI PERSO COGLIONE!!")
            balance = balance - scom
            print("SALDO: ",balance)
        elif sum == 1 or sum == 4 or sum == 5 or sum == 6 or sum == 8 or sum == 9 or sum == 10:
            mypoint = sum
            sum = rolldice()
            if sum == mypoint:
                print("HAI VINTO!\n")
                balance = balance + scom
                print("SALDO: ",balance)
            elif sum == 7:
                print("HAI PERSO COGLIONE!!")
                balance = balance - scom
                print("SALDO: ",balance)
            else:
                print("Non hai vinto nè perso nulla, ti è andata bene.\n")
        if balance != 0:
            print("Digita -1 per smettere di giocare, altrimenti digita 0 per continuare a giocare: ")
            fine = int(input())
    
def rolldice():
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    tot=dice1+dice2
    print("Il risultato dei tuoi dadi è:",tot)
    return tot

def bet():
    scom = int(input("Fai la tua scommessa "))
    while scom>balance:
        print("Hai scommesso troppo, riprova")
        scom = input()
    return scom

if __name__ == '__main__':
    main()