import os
import random

# Variabili
turni_possibili = ["0", "1"]
turno = random.choice(turni_possibili)
turno_precedente = turno
vittoria = False
mosse = turno + "|"
turni = 0
punti_giocatore = 0
punti_ia = 0
punti_pareggio = 0




segno = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def genera_campo():
    os.system("clear")
    print(nome_player+": "+str(punti_giocatore))
    print("IA: "+str(punti_ia))
    print("Pareggi: "+str(punti_pareggio))
    print(" ")
    print(f"       |       |       ")
    print(f"   {segno[1]}   |   {segno[2]}   |   {segno[3]}   ")
    print(f"       |       |       ")
    print(f"-----------------------")
    print(f"       |       |       ")
    print(f"   {segno[4]}   |   {segno[5]}   |   {segno[6]}   ")
    print(f"       |       |       ")
    print(f"-----------------------")
    print(f"       |       |       ")
    print(f"   {segno[7]}   |   {segno[8]}   |   {segno[9]}   ")
    print(f"       |       |       ")

def IA():
    global mossa
    partita = mosse
    migliore = "0|0|0"
    mossa ="0"

    if turni == 0:       
        mosse_possibili = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]                   
        mossa = random.choice(mosse_possibili)
        return mossa
    #verifica se deve bloccate o fare punto 
    #Verifca se fare punto
    #orizzontali

    if segno[1] == segno[2] and segno[3] == "3" and segno[1] == "O":
    	mossa = "3"
    elif segno[2] == segno[3] and segno[1] == "1" and segno[2] == "O":
    	mossa = "1"
    elif segno[3] == segno[1] and segno[2] == "2" and segno[3] == "O":
    	mossa = "2"
    	
    if segno[4] == segno[5] and segno[6] == "6" and segno[4] == "O":
    	mossa = "6"
    elif segno[5] == segno[6] and segno[4] == "4" and segno[5] == "O":
    	mossa ="4"
    elif segno[4] == segno[6] and segno[5] == "5" and segno[6] == "O":
    	 mossa="5"
    	 
    if segno[7] == segno[8] and segno[9] == "9" and segno[7] == "O":
    	 mossa="9"
    elif segno[8] == segno[9] and segno[7] == "7" and segno[8] == "O":
    	 mossa ="7"
    elif segno[7] == segno[9] and segno[8] == "8" and segno[9] == "O":
    	 mossa="8"
    	 
    #verticali
    if segno[1] == segno[4] and segno[7] == "7" and segno[1]=="O":
    	mossa = "7"
    elif segno[4] == segno[7] and segno[1] == "1" and segno[4]=="O":
    	mossa = "1"
    elif segno[1] == segno[7] and segno [4] == "4" and segno[1]=="O":
    	mossa = "4"
    	
    if segno[2] == segno[5] and segno[8] == "8" and segno[2]=="O":
    	mossa = "8"
    elif segno[5] == segno[8] and segno[2] == "2" and segno[5]=="O":
    	mossa ="2"
    elif segno[2] == segno[8] and segno[5] == "5" and segno[2]=="O":
    	 mossa="5"
    	 
    if segno[3] == segno[6] and segno[9] == "9" and segno[3]=="O":
    	 mossa="9"
    elif segno[6] == segno[9] and segno[3] == "3" and segno[6]=="O":
    	 mossa ="3"
    elif segno[3] == segno[9] and segno[6] == "6" and segno[3]=="O":
    	 mossa="6"
    	 
    	 
    #diagonali
    if segno[1] == segno[5] and segno[9] == "9" and segno[1] == "O":
    	 mossa="9"
    elif segno[5] == segno[9] and segno[1] == "1" and segno[5] == "O":
    	 mossa ="1"
    elif segno[1] == segno[9] and segno[5] == "5" and segno[1] == "O":
    	 mossa="5"
    	 
    if segno[3] == segno[5] and segno[7] == "7" and segno[3] == "O":
    	 mossa="7"
    elif segno[5] == segno[7] and segno[3] == "3" and segno[5] == "O":
    	 mossa ="3"
    elif segno[3] == segno[7]and segno[5] == "5" and segno[3] == "O":
    	 mossa="5"


    if mossa == "0":
        #verifica se parare
            #orizzontali

        if segno[1] == segno[2] and segno[3] == "3":
            mossa = "3"
        elif segno[2] == segno[3] and segno[1] == "1":
            mossa = "1"
        elif segno[3] == segno[1] and segno[2] == "2":
            mossa = "2"
            
        if segno[4] == segno[5] and segno[6] == "6":
            mossa = "6"
        elif segno[5] == segno[6] and segno[4] == "4":
            mossa ="4"
        elif segno[4] == segno[6] and segno[5] == "5":
            mossa="5"
            
        if segno[7] == segno[8] and segno[9] == "9":
            mossa="9"
        elif segno[8] == segno[9] and segno[7] == "7":
            mossa ="7"
        elif segno[7] == segno[9] and segno[8] == "8":
            mossa="8"
            
        #verticali
        if segno[1] == segno[4] and segno[7] == "7":
            mossa = "7"
        elif segno[4] == segno[7] and segno[1] == "1":
            mossa = "1"
        elif segno[1] == segno[7] and segno [4] == "4":
            mossa = "4"
            
        if segno[2] == segno[5] and segno[8] == "8":
            mossa = "8"
        elif segno[5] == segno[8] and segno[2] == "2":
            mossa ="2"
        elif segno[2] == segno[8] and segno[5] == "5":
            mossa="5"
            
        if segno[3] == segno[6] and segno[9] == "9":
            mossa="9"
        elif segno[6] == segno[9] and segno[3] == "3":
            mossa ="3"
        elif segno[3] == segno[9] and segno[6] == "6":
            mossa="6"
            
            
        #diagonali
        if segno[1] == segno[5] and segno[9] == "9":
            mossa="9"
        elif segno[5] == segno[9] and segno[1] == "1":
            mossa ="1"
        elif segno[1] == segno[9] and segno[5] == "5":
            mossa="5"
            
        if segno[3] == segno[5] and segno[7] == "7":
            mossa="7"
        elif segno[5] == segno[7] and segno[3] == "3":
            mossa ="3"
        elif segno[3] == segno[7]and segno[5] == "5":
            mossa="5"
            
    	 
    	 
    	 
    	 
    if mossa != "0":
    	return mossa
    	
    # Controllo win.txt per la miglior mossa
    with open("./ia_data/win.txt", "r") as file:
        for ln in file:
            if ln.startswith(partita):
                if int(ln.split("|")[2]) > int(migliore.split("|")[2]):
                    migliore = ln
                    

    mossa = migliore.replace(partita, "")
    mossa = mossa[:1]

    




     #se non trova mosse va a caso ma verifica il file lose.txt
    if mossa == "0":
     
        mosse_possibili = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
       
        with open("./ia_data/lose.txt", "r") as file:
            for ln in file:
                if ln.startswith(partita):
                    da_rimuovere = ln.replace(partita, "")[:1]  
                    if da_rimuovere in mosse_possibili:                       
                        mosse_possibili.remove(da_rimuovere)
                    else:
                        print("")

     

       
        if segno[1] != "1":
            mosse_possibili.remove("1")
         
        if segno[2] != "2":
            mosse_possibili.remove("2")
           
        if segno[3] != "3":
            mosse_possibili.remove("3")
         
        if segno[4] != "4":
            mosse_possibili.remove("4")
          
        if segno[5] != "5":
            mosse_possibili.remove("5")
          
        if segno[6] != "6":
            mosse_possibili.remove("6")
           
        if segno[7] != "7":
            mosse_possibili.remove("7")
 
        if segno[8] != "8":
            mosse_possibili.remove("8")
           
        if segno[9] != "9":
            mosse_possibili.remove("9")
            
    

        
        

        if not mosse_possibili:
            
            mosse_possibili = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
           
            if segno[1] != "1":
                mosse_possibili.remove("1")
              
            if segno[2] != "2":
                mosse_possibili.remove("2")
              
            if segno[3] != "3":
                mosse_possibili.remove("3")
           
            if segno[4] != "4":
                mosse_possibili.remove("4")
              
            if segno[5] != "5":
                mosse_possibili.remove("5")
               
            if segno[6] != "6":
                mosse_possibili.remove("6")
             
            if segno[7] != "7":
                mosse_possibili.remove("7")
             
            if segno[8] != "8":
                mosse_possibili.remove("8")
               
            if segno[9] != "9":
                mosse_possibili.remove("9")
               
     

        
        mossa = random.choice(mosse_possibili)
  

    
    return mossa

def effettua_mossa():
    global turno, mosse, mossa
    attuale_turno = turno
    
    while turno == attuale_turno:
        if turno == "0":
            mossa = input("Che mossa fai giocatore 1? ")
        else:
            print("Turno di IA")
            mossa = IA()
            os.system("sleep 1")
        
        if mossa.isdigit():
            mossa = int(mossa)
            if 1 <= mossa <= 9 and segno[mossa] == str(mossa):
                if turno == "0":
                    segno[mossa] = "X"
                    turno = "1"
                else:
                    segno[mossa] = "O"
                    turno ="0"                
                
                mosse += str(mossa)
                return 
            else:
                print("Mossa non valida!, hai inserito: "+str(mossa))
                mossa = "0"
        else:
            print("Mossa non valida!, hai inserito: "+str(mossa))
            mossa = "0"

def verifica_vittoria():
    global vittoria, vincitore, turni
    #orizzonatali
    if segno[1] == segno[2] and segno[2] == segno[3]:
        vittoria = True
        vincitore = segno[1]
    elif segno[4] == segno[5] and segno[5] == segno[6]:
        vittoria = True
        vincitore = segno[4]
    elif segno[7] == segno[8]  and segno[8] == segno[9]:
        vittoria= True
        vincitore = segno[7]

    #verticali
    if segno[1] == segno[4] and segno[4] == segno[7]:
        vittoria = True
        vincitore = segno[1]
    elif segno[2] == segno[5] and segno[5] == segno[8]:
        vittoria = True
        vincitore = segno[2]
    elif segno[3] == segno[6]  and segno[6] == segno[9]:
        vittoria= True
        vincitore = segno[3]    

    #diagonali
    if segno[1] == segno[5] and segno[5] == segno[9]:
        vittoria = True
        vincitore = segno[1]
    elif segno[3] == segno[5] and segno[5] == segno[7]:
        vittoria = True
        vincitore = segno[3]
    turni += 1
    if turni == 9:
        vincitore = None  # Pareggio
        vittoria = True

print("Ciao! Come ti chiami??")
nome_player = input("Inserisci: ")
os.system("clear")
print("Benevenuto!")
os.system("sleep 1")

while True:
    genera_campo()
    while not vittoria:
        effettua_mossa()
        genera_campo()
        verifica_vittoria()





    if vincitore == "X":
        punti_giocatore = punti_giocatore+1
        print(nome_player+" vince!")
        with open("./ia_data/lose.txt", "r") as file:
            data = file.readlines()
        trovato = False
        nuova_lista = []

        
        for ln in data:
            campi = ln.strip().split("|")
            if len(campi) == 3 and campi[0] + "|" + campi[1] == mosse:
                n = int(campi[2]) + 1
                nuova_lista.append(mosse + "|" + str(n) + "\n")
                trovato = True
            else:
                nuova_lista.append(ln)

        if not trovato:
            nuova_lista.append(mosse + "|1\n")

        
        with open("./ia_data/lose.txt", "w") as file:
            file.writelines(nuova_lista)

    elif vincitore == "O":
        print("L'IA vince!")
        punti_ia= punti_ia+1
      
        
        with open("./ia_data/win.txt", "r") as file:
            data = file.readlines()

        trovato = False
        nuova_lista = []

        
        for ln in data:
            campi = ln.strip().split("|")
            if len(campi) == 3 and campi[0] + "|" + campi[1] == mosse:
                n = int(campi[2]) + 1
                nuova_lista.append(mosse + "|" + str(n) + "\n")
                trovato = True
            else:
                nuova_lista.append(ln)

        if not trovato:
            nuova_lista.append(mosse + "|1\n")

        
        with open("./ia_data/win.txt", "w") as file:
            file.writelines(nuova_lista)

    else:
        print("Pareggio!")
        punti_pareggio = punti_pareggio+1
    input("Premi invio per continuare")

    if turno_precedente == "1":
    	turno = "0"
    	turno_precedente = "0"
    else:
    	turno = "1"
    	turno_precedente ="1"
    vittoria = False
    mosse = turno + "|"
    turni = 0

    segno[1]="1"
    segno[2]="2"
    segno[3]="3"
    segno[4]="4"
    segno[5]="5"
    segno[6]="6"
    segno[7]="7"
    segno[8]="8"
    segno[9]="9"

