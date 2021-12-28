from Crypto.Cipher import AES
from hashlib import md5
from pkg_resources import resource_filename, resource_listdir


def GetCodes(Passphrase, LabName):
    Key = md5(Passphrase.encode('utf8')).hexdigest().encode('utf8')

    DataFile = open(resource_filename(__name__,'Data/'+LabName+'.bin'), 'rb')
    Nonce, Tag, CipherText = [ DataFile.read(x) for x in (16, 16, -1) ]
    Cipher = AES.new(Key, AES.MODE_EAX, Nonce)

    Data = Cipher.decrypt_and_verify(CipherText, Tag).decode('utf8')
    return Data


def CreateLab(Passphrase, LabName):
    Key = md5(Passphrase.encode('utf8')).hexdigest().encode('utf8')

    Data = 'LAB: ' + LabName
    Cipher = AES.new(Key, AES.MODE_EAX)
    CipherText, Tag = Cipher.encrypt_and_digest(Data.encode('utf8'))

    DataFile = open(resource_filename(__name__,'Data/'+LabName+'.bin'), 'wb')
    [ DataFile.write(x) for x in (Cipher.nonce, Tag, CipherText) ]
    DataFile.close()

def AddCode(Passphrase, LabName, PATH):
    
    try:
        Data = GetCodes(Passphrase, LabName)
    except:
        print('!!!!!!!!!!! ERROR: LAB DOES NOT EXIST !!!!!!!!!!!')
    
    Data += '\n)!#!(\n'
    
    CodeTitle = input('Enter Title of the Code: ')+'\n'
    Language = input('Enter Languge in which Code is written: ')+'\n'
    Code = open(PATH,'r').read()

    Data += CodeTitle
    Data += Language + '%$^'
    Data += Code

    Key = md5(Passphrase.encode('utf8')).hexdigest().encode('utf8')
    Cipher = AES.new(Key, AES.MODE_EAX)
    CipherText, Tag = Cipher.encrypt_and_digest(Data.encode('utf8'))

    DataFile = open(resource_filename(__name__,'Data/'+LabName+'.bin'), 'wb')
    [ DataFile.write(x) for x in (Cipher.nonce, Tag, CipherText) ]
    DataFile.close()


def AccessCodes(Passphrase, LabName):

    try:
        Data = GetCodes(Passphrase, LabName)
    except:
        print('!!!!!!!!!!! ERROR: LAB DOES NOT EXIST !!!!!!!!!!!')

    Codes = Data.split('\n)!#!(\n')

    print('\n\n\n#### AVAILABLE CODES ####\n\n')
    for i in range(1,len(Codes)):
        CodeTitle, Language = Codes[i].split('\n')[:2]
        print(str(i) + '. ' + CodeTitle + ' - ' + Language + '\n')
        
    Choice = int(input(': '))
    
    print('\n\n\n####################### CODE #######################\n\n')
    print(Codes[Choice].split('%$^')[1])
    print('\n\n\n####################### CODE ENDS #######################')


def GetLabs():

    return resource_listdir(__name__,'Data/')