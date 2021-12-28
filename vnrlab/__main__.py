from vnrlab.utils import CreateLab, AddCode, AccessCodes, GetLabs

print('\n\n\n############## WELCOME TO VNRLAB ##############')
print('\n\n1. Access Codes\n2. Create New Lab\n3. Add New Code')
Choice = int(input('\n\n:'))

if Choice == 1:
    Labs = GetLabs()
    if Labs == []:
        print('\n\n#### NO LABS AVAILABLE ####')
        exit()

    print('\n\n#### AVAILABLE LABS ####\n\n')
    for i in range(0,len(Labs)):
        print(str(i+1)+ '. ' + Labs[i].replace('.bin',''))
    
    Choice = int(input('\n\n:'))

    if Choice <= len(Labs) and Choice > 0:
        LabName = Labs[Choice-1].replace('.bin','')  
        Passphrase = input('\n\n\nPassphrase: ')

        AccessCodes(Passphrase,LabName)
        exit()
    
    else:
        print('\n\n!!!! ERROR: LAB DOES NOT EXIST !!!!')
        exit()

elif Choice == 2:

    print('\n\n### CREATE NEW LAB ####')

    LabName = input('\nLab Name: ')
    Passphrase = input('\nPassphrase: ')
    CreateLab(Passphrase, LabName)

    print('\n\n!!!! NEW LAB CREATED !!!!')
    exit()

elif Choice == 3:

    print('\n\n### ADD NEW CODE ####')

    LabName = input('\nLab Name: ')
    Passphrase = input('\nPassphrase: ')
    PATH = input('\n\nComplete PATH to NEW CODE: ')
    AddCode(Passphrase, LabName, PATH)

    print('\n\n!!!! NEW CODE ADDED !!!!')
    exit()

else:
    exit()
